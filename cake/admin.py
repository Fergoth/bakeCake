from django.contrib import admin
from .models import (
    CakeLevel,
    CakeBerries,
    CakeDecor,
    CakeForm,
    CakeTopping,
    CakeOrder,
    CurentPhrasePrice,
)
import csv
from django.db.models import Sum
from django.http import HttpResponse


# Register your models here.
@admin.register(CakeLevel)
class CakeLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(CakeBerries)
class CakeBerriesAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(CakeDecor)
class CakeDecorAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(CakeForm)
class CakeFormAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(CakeTopping)
class CakeToppingAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(CurentPhrasePrice)
class CurentPhrasePriceAdmin(admin.ModelAdmin):
    list_display = ("price",)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            f"attachment; filename={meta.verbose_name_plural}.csv"
        )
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = []
            for field in field_names:
                value = getattr(obj, field)
                if callable(value):
                    value = value()
                row.append(str(value))
            writer.writerow(row)

        return response

    export_as_csv.short_description = "Экспорт в CSV"


@admin.register(CakeOrder)
class CakeOrderAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "expense_change_list.html"
    actions = ["export_as_csv"]
    list_display = ("level", "form", "topping", "berries", "decor", "price")

    def changelist_view(self, request, extra_context=None):
        total_amount = CakeOrder.objects.all().aggregate(total_sum=Sum("price"))
        context = {
            "total": total_amount.get("total_sum") or 0,
        }
        return super().changelist_view(request, extra_context=context)

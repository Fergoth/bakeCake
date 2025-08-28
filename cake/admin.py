from django.contrib import admin
from .models import CakeLevel, CakeBerries, CakeDecor, CakeForm, CakeTopping, CakeOrder, CurentPhrasePrice


# Register your models here.
@admin.register(CakeLevel)
class CakeLevelAdmin(admin.ModelAdmin):
    list_display = ("level", "price")


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


@admin.register(CakeOrder)
class CakeOrderAdmin(admin.ModelAdmin):
    list_display = ("level", "form", "topping", "berries", "decor", "price")

@admin.register(CurentPhrasePrice)
class CurentPhrasePriceAdmin(admin.ModelAdmin):
    list_display = ("price",)
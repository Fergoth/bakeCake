import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from .models import (
    CakeLevel,
    CakeForm,
    CakeBerries,
    CakeTopping,
    CakeDecor,
    CurentPhrasePrice,
    CakeOrder,
)


# Create your views here.
def index(request):
    cake_levels = CakeLevel.objects.all().filter(is_active=True)
    cake_forms = CakeForm.objects.all().filter(is_active=True)
    cake_berries = CakeBerries.objects.all().filter(is_active=True)
    cake_toppings = CakeTopping.objects.all().filter(is_active=True)
    cake_decors = CakeDecor.objects.all().filter(is_active=True)
    curent_phrase_price = CurentPhrasePrice.objects.all().first()
    context = {
        "all_context": {
            "levels": ["не выбрано"] + [i.name for i in cake_levels],
            "levels_price": [0] + [int(i.price) for i in cake_levels],
            "forms": ["не выбрано"] + [i.name for i in cake_forms],
            "forms_price": [0] + [int(i.price) for i in cake_forms],
            "berries": ["нет"] + [i.name for i in cake_berries],
            "berries_price": [0] + [int(i.price) for i in cake_berries],
            "toppings": ["не выбрано"] + [i.name for i in cake_toppings],
            "toppings_price": [0] + [int(i.price) for i in cake_toppings],
            "decors": ["нет"] + [i.name for i in cake_decors],
            "decors_price": [0] + [int(i.price) for i in cake_decors],
            "curent_phrase_price": int(curent_phrase_price.price),
        }
    }
    return render(request, "index.html", context=context)


def profile(request):
    return render(request, "profile.html")


@csrf_exempt
def save_order(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        level = CakeLevel.objects.get(name=data["level"])
        form = CakeForm.objects.get(name=data["form"])
        if data["berries"] == "нет":
            berries = None
        else:
            berries = CakeBerries.objects.get(name=data["berries"])
        topping = CakeTopping.objects.get(name=data["topping"])
        if data["decor"] == "нет":
            decor = None
        else:
            decor = CakeDecor.objects.get(name=data["decor"])
        order = CakeOrder.objects.create(
            level=level,
            form=form,
            berries=berries,
            topping=topping,
            decor=decor,
            phrase_on_cake=data["phrase_on_cake"],
            comment=data["comment"],
            date=f"{data['date']}T{data['time']}",
            courier_comment=data["courier_comment"],
            price=data["price"],
        )
        return JsonResponse({"status": "success", "order_id": order.id})

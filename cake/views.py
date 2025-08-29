from django.shortcuts import render
from .models import CakeLevel, CakeForm, CakeBerries, CakeTopping, CakeDecor, CurentPhrasePrice


# Create your views here.
def index(request):
    cake_levels = CakeLevel.objects.all()
    cake_forms = CakeForm.objects.all()
    cake_berries = CakeBerries.objects.all()
    cake_toppings = CakeTopping.objects.all()
    cake_decors = CakeDecor.objects.all()
    curent_phrase_price = CurentPhrasePrice.objects.all().first()
    context = {
        "all_context": {
            "levels": ["не выбрано"] + [i.level for i in cake_levels],
            "levels_price": [0] + [int(i.price) for i in cake_levels],
            "forms": ["не выбрано"] + [i.name for i in cake_forms],
            "forms_price": [0] + [int(i.price) for i in cake_forms],
            "berries": ["нет"] + [i.name for i in cake_berries],
            "berries_price": [0] + [int(i.price) for i in cake_berries],
            "toppings": ["не выбрано"] + [i.name for i in cake_toppings],
            "toppings_price": [0] + [int(i.price) for i in cake_toppings],
            "decors": ["нет"] + [i.name for i in cake_decors],
            "decors_price": [0] + [int(i.price) for i in cake_decors],
            "curent_phrase_price": int(curent_phrase_price.price)
        }
    }
    return render(request, "index.html", context=context)


def profile(request):
    return render(request, "profile.html")

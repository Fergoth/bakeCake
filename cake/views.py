from django.shortcuts import render
from .models import CakeLevel, CakeForm


# Create your views here.
def index(request):
    cake_levels = CakeLevel.objects.all()
    cake_forms = CakeForm.objects.all()
    context = {
        "all_context": {
            "levels": ["не выбрано"] + [i.level for i in cake_levels],
            "levels_price": [0] + [int(i.price) for i in cake_levels],
            "forms": ["не выбрано"] + [i.name for i in cake_forms],
            "forms_price": [0] + [int(i.price) for i in cake_forms],
        }
    }
    return render(request, "index.html", context=context)


def profile(request):
    return render(request, "profile.html")

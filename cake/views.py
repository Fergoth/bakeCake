from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "all_context": {
            "Levels": ["не выбрано", "1", "2", "3"],
        }
    }
    return render(request, "index.html", context=context)


def profile(request):
    return render(request, "profile.html")

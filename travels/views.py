from django.shortcuts import redirect


def travels(request):
    return redirect("https://yandex.ru/maps/?um=constructor%3A3af78ba526025db30b1f560e5b288d63c80827b3c2ca432fc318d754ef830ae5&source=constructorLink")

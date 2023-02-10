from django.shortcuts import redirect


def creations(request):
    return redirect("https://github.com/pbkrd?tab=repositories&q=&type=&language=&sort=name")

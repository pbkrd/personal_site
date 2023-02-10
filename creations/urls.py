from django.urls import path

from .views import *

urlpatterns = [
    path('', creations, name='creations'),
]
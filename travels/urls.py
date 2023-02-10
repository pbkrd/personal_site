from django.urls import path

from .views import *

urlpatterns = [
    path('', travels, name='travels'),
]
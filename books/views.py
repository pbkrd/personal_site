from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from books.models import Book
from books.utils import DataMixin


class BooksMain(DataMixin, ListView):
    model = Book
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title='Читаю')
        return {**context, **extra_con}

#
#     def get_queryset(self):
#         return Category.objects.all()


def books(request):
    return HttpResponse("Читаю")

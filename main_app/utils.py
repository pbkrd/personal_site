from .models import *

menu_header = [{'title': "Читаю", 'url_name': 'books'},
               {'title': "Смотрю", 'url_name': 'films'},
               {'title': "Пушетествую", 'url_name': 'travels'},
               {'title': "Создаю", 'url_name': 'creations'},
               {'title': "Пишу", 'url_name': 'posts'},
               ]


class DataMixin:
    paginate_by = 8

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu_header'] = menu_header
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

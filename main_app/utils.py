from .models import *

NON_PRINTABLE_APPS = ['Главная']


class DataMixinBase:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['apps'] = Application.objects.all()
        context['non_printable_apps'] = NON_PRINTABLE_APPS
        context.setdefault('app_selected', 0)

        # context.setdefault('cat_selected', 0)

        return context

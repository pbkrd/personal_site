from main_app.utils import DataMixinBase


class DataMixin(DataMixinBase):
    def get_user_context(self, **kwargs):
        context = super().get_user_context(**kwargs)
        context['app_selected'] = 2

        return context

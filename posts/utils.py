from main_app.utils import DataMixinBase


class DataMixin(DataMixinBase):
    paginate_by = 8

    def get_user_context(self, **kwargs):
        context = super().get_user_context(**kwargs)
        context['app_selected'] = 4
        context.setdefault('cat_selected', 0)

        return context

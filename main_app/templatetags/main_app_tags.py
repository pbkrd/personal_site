from django import template
from main_app.models import *

register = template.Library()


@register.inclusion_tag('main_app/list_categories.html')
def show_categories(cat_selected):
    cats = Category.objects.all()
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('main_app/list_categories_js.html')
def show_categories_btns(cats):
    return {"cats": cats}


@register.inclusion_tag('main_app/list_posts.html')
def show_posts(cat_id=None, amt=None):
    posts = Post.objects.filter(is_published=True).select_related('cat')
    posts = posts if not cat_id else posts.filter(cat__pk=cat_id)
    posts = posts[:amt]
    return {'posts': posts}

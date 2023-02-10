from django import template
from posts.models import Category, Post

register = template.Library()


def get_cats_and_amts_posts() -> tuple:
    cats = Category.objects.all().prefetch_related('post_set')
    amt_posts = sum(cat.post_set.count() for cat in cats)
    return cats, amt_posts


@register.inclusion_tag('posts/list_categories.html')
def show_categories(cat_selected):
    cats, amt_posts = get_cats_and_amts_posts()
    return {"cat_selected": cat_selected, "cats": cats, "amt_posts": amt_posts}


@register.inclusion_tag('posts/list_categories_js.html')
def show_categories_btns():
    cats, amt_posts = get_cats_and_amts_posts()
    return {"cats": cats, "amt_posts": amt_posts}


@register.inclusion_tag('posts/list_posts.html')
def show_posts(cat_id=None, amt=None, last=None, posts=None):
    if posts is None:
        posts = Post.objects.filter(is_published=True).select_related('cat')
        posts = posts if not cat_id else posts.filter(cat__pk=cat_id)
        posts = posts[:amt]
    return {'posts': posts, 'last': last}
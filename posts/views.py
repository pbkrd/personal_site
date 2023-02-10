from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from posts.models import Post, Category
from posts.utils import DataMixin


class ShowPosts(DataMixin, ListView):
    model = Post
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title='Пишу')
        return {**context, **extra_con}

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('cat')


class ShowCategoryPosts(ShowPosts):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['cat_slug'])
        extra_con = self.get_user_context(title='Категория - ' + cat.name,
                                          cat_selected=cat.pk)
        return {**context, **extra_con}

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'posts/post.html'
    slug_url_kwarg = 'cat_slug'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title=context['post'])
        return {**context, **extra_con}
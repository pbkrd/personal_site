from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from .forms import RegisterUserForm, LoginUserForm, ContactForm
from .models import Post, Category
from .services import get_all_posts
from .utils import DataMixin

menu_header = [{'title': "О сайте", 'url_name': 'about'},
               {'title': "Добавить статью", 'url_name': 'add_page'},
               {'title': "Обратная связь", 'url_name': 'contact'}
               ]

menu = [{'title': "Читаю", 'url_name': 'books'},
        {'title': "Смотрю", 'url_name': 'films'},
        {'title': "Пушетествую", 'url_name': 'travels'},
        {'title': "Создаю", 'url_name': 'creations'}
        ]

menu_tabpanel = [{'title': "Все категории", 'posts': 'about'},
                 {'title': "1 категория", 'posts': 'add_page'},
                 {'title': "2 категория", 'posts': 'contact'},
                 ]


class PageHome(DataMixin, ListView):
    model = Category
    template_name = 'main_app/index.html'
    context_object_name = 'cats'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title='Главная страница')
        return {**context, **extra_con}

    def get_queryset(self):
        return Category.objects.all()


class ShowPosts(DataMixin, ListView):
    model = Post
    template_name = 'main_app/posts.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title='Категории')
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
    template_name = 'main_app/post.html'
    slug_url_kwarg = 'cat_slug'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title=context['post'])
        return {**context, **extra_con}


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'main_app/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title="Обратная связь")
        return {**context, **extra_con}

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_app/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title="Регистрация")
        return {**context, **extra_con}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main_app/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title="Авторизация")
        return {**context, **extra_con}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def about(request):
    return render(request, 'main_app/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")


def books(request):
    return HttpResponse("Читаю")


def films(request):
    return HttpResponse("Смотрю")


def travels(request):
    return HttpResponse("Путешествую")


def posts(request):
    return HttpResponse("Пишу")


def creations(request):
    return HttpResponse("https://github.com/pbkrd?tab=repositories&q=&type=&language=&sort=name")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

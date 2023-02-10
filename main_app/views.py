from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView

from posts.models import Category
from .forms import RegisterUserForm, LoginUserForm, ContactForm
from .models import Application
from .utils import DataMixinBase


class PageHome(DataMixinBase, ListView):
    model = Application
    template_name = 'main_app/index.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_con = self.get_user_context(title='Главная страница',
                                          cats=Category.objects.all())
        return {**context, **extra_con}


class ContactFormView(DataMixinBase, FormView):
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


class RegisterUser(DataMixinBase, CreateView):
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


class LoginUser(DataMixinBase, LoginView):
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


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

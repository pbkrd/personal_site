from django.urls import path

from .views import *

urlpatterns = [
    path('', PageHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('books/', books, name='books'),
    path('films/', films, name='films'),
    path('travels/', travels, name='travels'),
    path('posts/all/', ShowPosts.as_view(), name='posts'),
    path('posts/<slug:cat_slug>/', ShowCategoryPosts.as_view(), name='show_category'),
    path('post/<slug:cat_slug>/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('creations/', creations, name='creations'),
]
from django.urls import path

from .views import *

urlpatterns = [
    path('all/', ShowPosts.as_view(), name='posts'),
    path('<slug:cat_slug>/', ShowCategoryPosts.as_view(), name='show_category'),
    path('<slug:cat_slug>/<int:post_id>/', ShowPost.as_view(), name='post'),
]
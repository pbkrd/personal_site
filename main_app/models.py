from django.conf import settings
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="Текст поста")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Фото")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, null=True, verbose_name="Публикация")
    published_date = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'cat_slug': self.cat.slug, 'post_id': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']




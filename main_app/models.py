from django.db import models
from django.urls import reverse


class Application(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(self.slug)

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'
        ordering = ['-id']
from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    author = models.TextField(verbose_name="Автор")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, verbose_name="Обложка")
    read_date = models.DateTimeField(default=timezone.now, verbose_name="Дата прочтения")
    format_read = models.CharField(max_length=1, choices=(('C', 'classic'), ('A', 'audio')))
    # review = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, verbose_name="Рецензия")
    is_on_shelf = models.BooleanField(default=False, verbose_name="На полке")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'cat_slug': self.cat.slug, 'post_id': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-id']

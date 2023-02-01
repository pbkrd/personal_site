# Generated by Django 4.1.4 on 2023-01-11 08:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='Текст поста')),
                ('photo', models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, null=True, verbose_name='Публикация')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_app.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-id'],
            },
        ),
    ]
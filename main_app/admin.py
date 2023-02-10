from django.contrib import admin
from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', 'slug')


admin.site.register(Application, ApplicationAdmin)

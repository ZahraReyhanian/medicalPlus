from django.contrib import admin
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'short_body', 'image']
    list_display_links = ['title']
    list_per_page = 10
    search_fields = ['title']

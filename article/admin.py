from django.contrib import admin
from django.utils.html import format_html
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
    readonly_fields = ['thumbnail', 'viewCount', 'commentCount']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thubnail" />')
        else:
            return ''

    class Media:
        css = {
            'all': ['article/styles.css']
        }

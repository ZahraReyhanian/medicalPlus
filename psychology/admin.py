from django.contrib import admin
from django.utils.html import format_html
from . import models

@admin.register(models.Test)
class TestAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['title', 'questions', 'type', 'price']
    list_editable = ['price']
    list_per_page = 10
    search_fields = ['title']
    readonly_fields = ['thumbnail', 'viewCount']

    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f'<img src="{instance.image.url}" class="thubnail" />')
        else:
            return ''

    class Media:
        css = {
            'all': ['test/styles.css']
        }


@admin.register(models.TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'number']
    list_editable = ['question']
    list_per_page = 20
    search_fields = ['question']
    list_display_links = ['id']
    ordering = ['id', 'number']

@admin.register(models.TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'test', 'result', 'grade']
    list_editable = ['result', 'grade']
    list_display_links = ['id']
    ordering = ['-id']
    list_per_page = 10


@admin.register(models.TestUserStatus)
class TestUserStatusAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'status']
    readonly_fields = ['result']
    list_editable = ['status']
    ordering = ['-id']
    list_per_page = 10
from django.contrib import admin
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


from django.contrib import admin
from . import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content_object', 'status', 'amount', 'track_id', 'created_at', 'updated_at']
    list_display_links = ['id']
    list_per_page = 10
    search_fields = ['user__username']
    readonly_fields = ['content_object', 'created_at', 'updated_at']

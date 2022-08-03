from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserAccessContent

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "first_name", "last_name"),
            },
        ),
    )

@admin.register(UserAccessContent)
class UserAccessContentAdmin(admin.ModelAdmin):
    readonly_fields = ['content_object']
    list_display = ['id', 'user', 'content_object', ]
    list_display_links = ['id']
    list_per_page = 20
    search_fields = ['user']
    autocomplete_lookup_fields = {
        'content_object': [['content_type', 'object_id']],
    }
from django.contrib import admin
from . import models


class SymptomFormulaInline(admin.TabularInline):
    # autocomplete_fields = ['option']
    min_num = 1
    max_num = 10
    model = models.SymptomFormula
    extra = 0

@admin.register(models.Symptom)
class SymptomAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }
    inlines = [SymptomFormulaInline]
    list_display = ['name', 'adult', 'gender']
    list_editable = ['gender']
    list_display_links = ['name']
    list_per_page = 20
    search_fields = ['name']
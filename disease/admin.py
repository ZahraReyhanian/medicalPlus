from django.contrib import admin
from . import models

class SymptomFormulaOptionInline(admin.StackedInline):
    model = models.SymptomFormulaOption
    min_num = 1

@admin.register(models.SymptomFormula)
class SymptomFormulaInline(admin.ModelAdmin):
    inlines = [SymptomFormulaOptionInline]
    list_display = ['id', 'symptom', 'result', 'sum']
    search_fields = ['symptom']
    list_display_links = ['id']

@admin.register(models.Symptom)
class SymptomAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['name']
    }
    list_display = ['name', 'adult', 'gender']
    list_editable = ['gender']
    list_display_links = ['name']
    list_per_page = 20
    search_fields = ['name']
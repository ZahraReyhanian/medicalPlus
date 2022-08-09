from django.contrib import admin
from . import models

class SymptomFormulaOptionInline(admin.StackedInline):
    model = models.SymptomFormulaOption
    autocomplete_fields = ['option']
    min_num = 1

@admin.register(models.SymptomFormula)
class SymptomFormulaInline(admin.ModelAdmin):
    inlines = [SymptomFormulaOptionInline]
    list_display = ['id', 'symptom', 'result', 'sum']
    search_fields = ['symptom']
    list_display_links = ['id']

@admin.register(models.SymptomQuestionOption)
class SymptomQuestionOptionAdmin(admin.ModelAdmin):
    list_display_links = ['id']
    list_display = ['id', 'option']
    search_fields = ['id', 'option']
class SymptomQuestionOptionInline(admin.TabularInline):
    model = models.SymptomQuestionOption
    min_num = 1

@admin.register(models.SymptomQuestion)
class SymptomQuestionAdmin(admin.ModelAdmin):
    inlines = [SymptomQuestionOptionInline]
    list_display = ['id', 'symptom', 'question', 'gender']
    list_editable = ['gender']
    search_fields = ['symptom', 'question', 'gender']
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
from django.db import models
from core.fields import IntegerRangeField

class Symptom(models.Model):
    GENDER_BOTH = 'B'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_BOTH, 'both'),
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    ]

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, allow_unicode=True)
    adult = models.BooleanField()
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, default=GENDER_BOTH
    )
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name

class SymptomQuestion(models.Model):
    GENDER_BOTH = 'B'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_BOTH, 'both'),
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    ]
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE, related_name='questions')
    number = IntegerRangeField(min_value=1)
    question = models.TextField()
    numberOfOption = IntegerRangeField(min_value=1)
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, default=GENDER_BOTH
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class SymptomQuestionOption(models.Model):
    GENDER_BOTH = 'B'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_BOTH, 'both'),
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    ]
    question = models.ForeignKey(SymptomQuestion, on_delete=models.CASCADE, related_name='options')
    option = models.TextField()
    value = models.IntegerField(default=1)
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, default=GENDER_BOTH
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.option


class SymptomFormula(models.Model):
    GENDER_BOTH = 'B'
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = [
        (GENDER_BOTH, 'both'),
        (GENDER_MALE, 'male'),
        (GENDER_FEMALE, 'female'),
    ]
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE, related_name='formulas')
    sum = models.IntegerField()
    result = models.TextField()
    gender = models.CharField(
        max_length=5, choices=GENDER_CHOICES, default=GENDER_BOTH
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return self.result

class SymptomFormulaOption(models.Model):
    formula = models.ForeignKey(SymptomFormula, on_delete=models.CASCADE, related_name='options')
    option = models.ForeignKey(SymptomQuestionOption, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.option)




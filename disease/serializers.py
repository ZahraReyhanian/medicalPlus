from rest_framework import serializers
from .models import Symptom, SymptomFormula, SymptomFormulaOption, SymptomQuestion, SymptomQuestionOption

class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = ['id', 'slug', 'name', 'adult','gender', 'view_count']


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SymptomQuestionOption
        fields = ['id', 'question', 'option', 'value', 'gender']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = SymptomQuestion
        fields = ['id', 'symptom', 'number', 'question', 'numberOfOption', 'options', 'gender']


class SymptomQuestionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Symptom
        fields = ['id', 'slug', 'name', 'adult', 'gender', 'view_count', 'questions']


class SymptomFormulaOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomFormulaOption
        fields = ['option']

class FormulaSerializer(serializers.ModelSerializer):
    options = SymptomFormulaOptionSerializer(many=True)
    class Meta:
        model = SymptomFormula
        fields = ['id', 'sum', 'result', 'symptom', 'options']


from rest_framework import serializers
from .models import Test, TestQuestion

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'description', 'slug', 'questions', 'type', 'answers', 'tags']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['number', 'question', 'numberOfAnswer', 'answers']


class TestQuestionSerializer(serializers.ModelSerializer):
    testquestions = QuestionSerializer(many=True)
    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'slug', 'questions', 'testquestions', 'answers']



from rest_framework import serializers
from .models import Test, TestQuestion, TestResult

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'image', 'viewCount', 'description', 'body', 'slug', 'questions', 'type', 'price', 'answers', 'tags', 'contentType']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['number', 'question', 'numberOfAnswer', 'answers']


class TestQuestionSerializer(serializers.ModelSerializer):
    testquestions = QuestionSerializer(many=True)
    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'slug', 'viewCount','questions', 'testquestions', 'answers']


class ResultSerializer(serializers.ModelSerializer):
    test = TestSerializer()
    class Meta:
        model = TestResult
        fields = ['result', 'grade', 'test']


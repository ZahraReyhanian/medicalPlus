from rest_framework import serializers

from core.models import UserAccessContent
from .models import Test, TestQuestion, TestResult

class TestSerializer(serializers.ModelSerializer):
    access = serializers.SerializerMethodField()

    def get_access(self, test: Test):
        if test.type == 'free':
            return True

        user_id = 0
        if 'user_id' in self.context:
            user_id = self.context['user_id']

        if user_id == 0:
            return False
            
        return UserAccessContent.objects.filter(
                                    content_type=test.contentType, 
                                    object_id=test.id,
                                    user_id=user_id).exists()

    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'image', 'viewCount', 'description', 'body', 'slug', 'questions', 'type', 'price', 'answers', 'tags', 'contentType', 'access']


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



class TestUserSerializer(TestSerializer):
    email = serializers.SerializerMethodField()

    def get_email(self, test: Test):
        if 'user_email' in self.context:
            return self.context['user_email']
        else:
            return ""
    class Meta:
        model = Test
        fields = ['id', 'email', 'slug', 'title', 'image', 'viewCount', 'description', 'body', 'slug', 'questions', 'type', 'price', 'answers', 'tags', 'contentType', 'access']

from rest_framework import serializers
import json
from .models import Test

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = ['id', 'slug', 'title', 'description', 'slug', 'questions', 'type', 'answers', 'tags']



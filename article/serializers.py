import json
from rest_framework import serializers
from jalali_date import date2jalali, datetime2jalali

from core.serializers import FixAbsolutePathSerializer

from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    body = FixAbsolutePathSerializer()
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, article: Article):
        date = json.dumps(article.get_jalali_created_at(), default=str)
        return date[1:-2]

    def get_updated_at(self, article: Article):
        date = json.dumps(article.get_jalali_updated_at(), default=str)
        return date[1:-2]

    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'slug', 'lang', 'body', 'short_body', 'image', 'viewCount', 'commentCount', 'created_at', 'updated_at']

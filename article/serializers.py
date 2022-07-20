import json
from rest_framework import serializers
from jalali_date import date2jalali, datetime2jalali

from core.serializers import FixAbsolutePathSerializer

from .models import Article, SaveArticle

class ArticleSerializer(serializers.ModelSerializer):
    body = FixAbsolutePathSerializer()
    user = serializers.StringRelatedField()
    saved = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, article: Article):
        date = json.dumps(article.get_jalali_created_at(), default=str)
        return date[1:-2]

    def get_updated_at(self, article: Article):
        date = json.dumps(article.get_jalali_updated_at(), default=str)
        return date[1:-2]

    def get_saved(self, article: Article):
        user_id = 0
        if 'user_id' in self.context:
            user_id = self.context['user_id']

        if(user_id == 0):
            return 0
        saved = SaveArticle.objects.filter(user_id=user_id, article_id=article.id).count()
        return saved

    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'slug', 'lang', 'body', 'short_body', 'image', 'saved','viewCount', 'commentCount', 'created_at', 'updated_at']

import profile
from venv import create
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreatePasswordRetypeSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from django.conf import settings
from django.db import transaction

from core.models import User, UserProfile
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class UserImageSerializer(serializers.ModelSerializer):
    def save(self, **kwargs):
        avatar = self.validated_data['avatar']
        user_id = self.context['user_id']
        
        with transaction.atomic():
            UserProfile.objects.filter(user_id=user_id).delete()
            profile = UserProfile.objects.create(user_id=user_id, avatar=avatar)

            return profile

    class Meta:
        model = UserProfile
        fields = ['avatar']

     

class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(settings.SEARCH_PATTERN, settings.REPLACE_WITH)
        return text
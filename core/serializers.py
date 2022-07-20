from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreatePasswordRetypeSerializer as BaseUserCreateSerializer

from rest_framework import serializers
from django.conf import settings
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(settings.SEARCH_PATTERN, settings.REPLACE_WITH)
        return text
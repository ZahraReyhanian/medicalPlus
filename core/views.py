from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from rest_framework import status
from django.shortcuts import render
from django.contrib.admin.options import get_content_type_for_model
from psychology.serializers import TestSerializer
from .models import User, UserAccessContent, UserProfile
from .serializers import UserImageSerializer, UserSerializer
from psychology.models import Test



class UserImageViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [IsAuthenticated]
    # set permission (all for admin user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user.id
        return context

    def create(self, request, *args, **kwargs):
        serializer = UserImageSerializer(
            data=request.data,
            context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        serializer = UserImageSerializer(profile, context=self.get_serializer_context())
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserTestAccessViewSet(mixins.ListModelMixin,
                            GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TestSerializer

    def get_queryset(self):
        accesses = UserAccessContent.objects.filter(
            user_id=self.request.user.id,
            content_type=get_content_type_for_model(Test)
        ).only('object_id')
        access_ids = list(access.object_id for access in accesses)
        tests = Test.objects.filter(id__in=access_ids)
        return tests

    def get_serializer_context(self):
        return {
            'user_id': self.request.user.id,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
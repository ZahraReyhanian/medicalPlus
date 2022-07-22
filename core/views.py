from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from django.shortcuts import render
from .models import User, UserProfile
from .serializers import UserImageSerializer, UserSerializer



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

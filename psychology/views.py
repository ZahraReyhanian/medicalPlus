from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from psychology.serializers import TestSerializer

from .models import Test

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
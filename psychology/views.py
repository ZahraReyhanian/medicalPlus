from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from psychology.serializers import TestQuestionSerializer, TestSerializer

from .models import Test

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestQuestionViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = TestQuestionSerializer

    def get_queryset(self):
        return Test.objects.all()
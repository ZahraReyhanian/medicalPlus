from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from .serializers import TestQuestionSerializer, TestSerializer
from .pagination import DefaultPagination
from .models import Test

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

class TestQuestionViewSet(RetrieveModelMixin, GenericViewSet):
    serializer_class = TestQuestionSerializer

    def get_queryset(self):
        return Test.objects.all()
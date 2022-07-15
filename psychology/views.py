from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .serializers import TestQuestionSerializer, TestSerializer
from .pagination import DefaultPagination
from .models import Test

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def questions(self, request, pk):
        test = Test.objects.filter(pk=pk).get()
        serializer = TestQuestionSerializer(test)
        return Response(serializer.data)

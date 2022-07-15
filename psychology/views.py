from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .serializers import ResultSerializer, TestQuestionSerializer, TestSerializer
from .pagination import DefaultPagination
from .models import Test, TestResult

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

    #todo save user status
    #todo update viewCount

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def questions(self, request, pk):
        test = Test.objects.filter(pk=pk).get()
        serializer = TestQuestionSerializer(test)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def questionsresult(self, request, pk):
        #todo update user result
        result = request.data["result"]
        testresult = TestResult.objects.filter(test_id=pk).filter(Q(grade__gte=result)).order_by('grade').first()
        serializer = ResultSerializer(testresult)
        return Response(serializer.data)

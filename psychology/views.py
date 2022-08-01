from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import ResultSerializer, TestQuestionSerializer, TestSerializer
from .pagination import DefaultPagination
from .models import Test, TestResult

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'PUT']:
            return [IsAdminUser()]
        
        # print(self.request.path) # /psychology/tests/4/
        #todo check prmission to store test
        return [AllowAny()]

    #todo save user status
    #todo update viewCount

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Test.objects.filter(pk=kwargs['pk']).update(viewCount=instance.viewCount + 1)
        serializer = TestSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)
    

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

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def checkout(self, request, pk):
        test = Test.objects.filter(pk=pk).get()
        test_type = ContentType.objects.get_for_model(test)
        if (test.type != 'free' and not request.user.accessContent(test.id, test_type)):
            serializer = TestSerializer(test)
            return Response(serializer.data)
        else:
            return HttpResponseNotFound("Not found!")

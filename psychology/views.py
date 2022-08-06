from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseForbidden, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from .serializers import ResultSerializer, TestQuestionSerializer, TestSerializer, TestUserSerializer
from .pagination import DefaultPagination
from .models import Test, TestResult, TestUserStatus

# Create your views here.
class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        elif self.action in ['questionsresult', 'questions', 'checkout']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    #todo save user status

    def hasAccess(self, request, pk):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        test = Test.objects.filter(pk=pk).get()
        test_type = ContentType.objects.get_for_model(test)
        if (test.type != 'free' and not request.user.accessContent(test.id, test_type)):
            return False
        return True

    def get_serializer_context(self):
        user_id = 0
        if self.request.user:
            user_id = self.request.user.id

        return {
            'user_id': user_id,
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }



    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Test.objects.filter(pk=kwargs['pk']).update(viewCount=instance.viewCount + 1)
        
        context=self.get_serializer_context()
        context['has_access'] = self.hasAccess(request, kwargs['pk'])

        serializer = TestSerializer(instance, context=context)
        return Response(serializer.data)
    

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def questions(self, request, pk):
        if self.hasAccess(request, pk):
            test = self.get_object()
            TestUserStatus.objects.create(user=request.user, test=test, status=TestUserStatus.STATUS_GETSTART)
            serializer = TestQuestionSerializer(test)
            return Response(serializer.data)
        else:
            return HttpResponseForbidden("Forbidden!", status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def questionsresult(self, request, pk):
        if self.hasAccess(request, pk):
            result = request.data["result"]
            testresult = TestResult.objects.filter(test_id=pk).filter(Q(grade__gte=result)).order_by('grade').first()

            TestUserStatus.objects.filter(user=request.user, test_id=pk)\
                                    .update(status=TestUserStatus.STATUS_SUBMITTED,
                                            result=testresult.result)

            serializer = ResultSerializer(testresult)
            return Response(serializer.data)
        else:
            return HttpResponseForbidden("Forbidden!", status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
    def checkout(self, request, pk):
        if not self.hasAccess(request, pk):
            context = self.get_serializer_context()
            context["user_email"] = self.request.user.email
            serializer = TestUserSerializer(self.get_object(), context=context)
            return Response(serializer.data)
        else:
            return HttpResponseNotFound("Not found!", status=status.HTTP_404_NOT_FOUND)

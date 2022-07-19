from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from .pagination import DefaultPagination
from .serializers import ArticleSerializer
from .models import Article

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.select_related('user').order_by('-updated_at').all()
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'PUT', 'POST']:
            return [IsAdminUser()]
        return [AllowAny()]

    @action(detail=False, methods=['GET'], permission_classes=[])
    def earliest(self, request):
        articles = Article.objects.select_related('user').order_by('-created_at').all()[:3]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


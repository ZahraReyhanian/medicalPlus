from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .pagination import DefaultPagination
from .serializers import ArticleSerializer
from .models import Article, SaveArticle

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.select_related('user').order_by('-updated_at').all()
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'PUT']:
            return [IsAdminUser()]
        return [AllowAny()]

        #todo set permission for create

    @action(detail=False, methods=['GET'], permission_classes=[AllowAny])
    def earliest(self, request):
        articles = Article.objects.select_related('user').order_by('-created_at').all()[:3]
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'], permission_classes=[IsAuthenticated])
    def savearticle(self, request, pk):
        obj, created = SaveArticle.objects.get_or_create(user_id=request.user.id, article_id=pk)
        if not created:
            obj.delete()
        return Response("ok")


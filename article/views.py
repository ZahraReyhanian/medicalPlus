from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .pagination import DefaultPagination
from .serializers import ArticleSerializer, RetrieveArticleSerializer
from .models import Article, SaveArticle

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.select_related('user').order_by('-updated_at').all()
    serializer_class = ArticleSerializer

    pagination_class = DefaultPagination

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Article.objects.filter(pk=kwargs['pk']).update(viewCount=instance.viewCount + 1)
        serializer = RetrieveArticleSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)

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
        

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'earliest']:
            permission_classes = [AllowAny]
        elif self.action in ['savearticle', 'saves']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
    

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

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def saves(self, request):
        articles = Article.objects.select_related('user').prefetch_related('saves').filter(saves__user_id=request.user.id)
        serializer = ArticleSerializer(articles, many=True, context=self.get_serializer_context())
        return Response(serializer.data)



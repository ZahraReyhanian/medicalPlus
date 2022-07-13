from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.ArticleViewSet, basename='articles')

urlpatterns = router.urls
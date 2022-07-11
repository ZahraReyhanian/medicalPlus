from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('tests', views.TestViewSet, basename='tests')
router.register('questions', views.TestQuestionViewSet, basename='questions')

urlpatterns = router.urls
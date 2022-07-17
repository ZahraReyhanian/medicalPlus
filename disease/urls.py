from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('symptoms', views.SymptomViewSet, basename='symptoms')

urlpatterns = router.urls
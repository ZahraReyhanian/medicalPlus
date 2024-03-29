from django.urls import path
from .views import MyTokenObtainPairView, UserImageViewSet, UserTestAccessViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('userprofile', UserImageViewSet, basename='upload_image')
router.register('useraccesstests', UserTestAccessViewSet, basename='useraccesstests')


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
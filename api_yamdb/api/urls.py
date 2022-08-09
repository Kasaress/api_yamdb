from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import RegisterView, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', RegisterView),
    path('v1/', include(router_v1.urls)),
]

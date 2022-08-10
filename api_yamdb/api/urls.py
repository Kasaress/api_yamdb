from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MeView, RegisterView, TokenView, UserViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/signup/', RegisterView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
    path('v1/users/me/', MeView.as_view()),
    path('v1/', include(router_v1.urls)),
]

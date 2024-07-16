from django.urls import path   # type: ignore
from rest_framework.routers import DefaultRouter   # type: ignore

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserUpdateAPIView, UserDeleteAPIView, UserRetrieveAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='users_delete'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls

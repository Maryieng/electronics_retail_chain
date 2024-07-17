from rest_framework import generics, status   # type: ignore
from rest_framework.permissions import AllowAny, IsAuthenticated   # type: ignore

from users.models import User
from users.permissions import IsAdmin
from users.serializers import UserSerializer
from rest_framework.response import Response   # type: ignore


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """Переопределение метода для сохранения пароля в БД"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.is_active = True
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Изменение пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated | IsAdmin,]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр данных пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated | IsAdmin,]


class UserDeleteAPIView(generics.DestroyAPIView):
    """Удаление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdmin,]

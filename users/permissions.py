from rest_framework.permissions import BasePermission   # type: ignore


class IsAdmin(BasePermission):
    """ проверка прав на администратора """
    def has_permission(self, request, view):
        return request.user.is_staff

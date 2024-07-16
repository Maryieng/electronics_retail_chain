from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "Вы не имеете прав администратора"

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(BasePermission):
    message = "Вы не имеете прав автора"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner

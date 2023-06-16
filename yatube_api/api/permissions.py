from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Класс разрешений, запрещающий изменение записи не автором. """
    def has_object_permission(self, request, _, obj):  # вместо '_' стоит views
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

from rest_framework import permissions


class IsSuperuser(permissions.BasePermission):
    message = 'Нужны права SuperUser'

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsAdmin(permissions.BasePermission):
    message = 'Нужны права администратора'

    def has_permission(self, request, view):
        return request.user.role == 'admin'

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'admin'


class IsModerator(permissions.BasePermission):
    message = 'Нужны права модератора'

    def has_permission(self, request, view):
        return request.user.role == 'moderator'

    def has_object_permission(self, request, view, obj):
        return request.user.role == 'moderator'


class IsAuthor(permissions.BasePermission):
    message = 'Для этого нужно быть автором, администратором, или модератором'
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Нужны права администратора'

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.role == 'admin'
        )

    def has_object_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user.role == 'admin'
        )

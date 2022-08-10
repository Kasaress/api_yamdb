from rest_framework import permissions


class IsAdminOrSuperuser(permissions.BasePermission):
    message = 'Нужны права SuperUser или admin'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_admin


class IsSuperuser(permissions.BasePermission):
    message = 'Нужны права SuperUser'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser


class IsAdmin(permissions.BasePermission):
    message = 'Нужны права администратора'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_superuser


class IsModerator(permissions.BasePermission):
    message = 'Нужны права модератора'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'moderator'


class IsAuthor(permissions.BasePermission):
    message = 'Для этого нужно быть автором, администратором, или модератором'
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Нужны права администратора'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and (
                    request.user.is_admin or request.user.is_superuser)))



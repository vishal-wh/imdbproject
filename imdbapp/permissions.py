from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    No permission for anonymous user
    For super user, read write permission
    For authenticate normal user, read only permission
    """
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        if request.user.is_active and request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            if request.user.is_authenticated and not request.user.is_superuser and request.user.is_active:
                return True
        return False

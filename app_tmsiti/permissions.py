from rest_framework.permissions import BasePermission

class IsSuperuserOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in ('GET', 'OPTIONS'):
            return True
        return request.user.is_superuser
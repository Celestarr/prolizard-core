from rest_framework.permissions import BasePermission, IsAuthenticated

from apps.core.models import User


class IsObjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        del view

        if isinstance(obj, User):
            return request.user == obj

        return False


class IsUnauthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        return not super().has_permission(request, view)


class IsMember(IsAuthenticated):
    def has_permission(self, request, view):
        authenticated = super().has_permission(request, view)

        return authenticated and request.user.user_type == "Member"

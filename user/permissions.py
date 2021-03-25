from rest_framework import permissions


class IsAuthenticatedOrOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.user.is_authenticated:
            return request.user.pk == obj.user.pk

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user== request.user

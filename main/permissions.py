from rest_framework.permissions import BasePermission


class PublicEndpoint(BasePermission):
    @classmethod
    def has_permission(cls, request, view):
        return True

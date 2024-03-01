from rest_framework.permissions import BasePermission


class IsAdminOrAuthenticatedUser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.is_staff
        else:
            return request.user.is_authenticated

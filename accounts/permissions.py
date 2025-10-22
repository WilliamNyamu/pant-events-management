from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsUserorReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # obj(user instance).id should be equal with the authenticated user id
        return obj.id == request.user.id

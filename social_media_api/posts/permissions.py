from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow owners of an object to edit it. Read-only for others.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only to the object's author
        return obj.author == request.user

from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD']:
            return True
        return request.user.is_authenticated

class IsAdminToVerify(BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action == "verify" and request.user.profile.role == "admin":
            return True
        return False

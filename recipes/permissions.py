from rest_framework.permissions import BasePermission

class IsUploader(BasePermission):
    message = 'You must be the uploader of this recipe to continue.'
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.profile.user == request.user
from rest_framework.permissions import BasePermission

class IsPostOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET','HEAD','OPTOINS'):
            return True
        
        if obj.owner == request.user:
            return True
        
        return False
        
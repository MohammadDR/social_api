from rest_framework import permissions

class IsCommentOwnerOrPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.owner == request.user: # owner of comment
            return True
        
        if obj.post.owner == request.user and request.method == 'DELETE': # owner of post can only delete his post's commments
            return True
        
        return False
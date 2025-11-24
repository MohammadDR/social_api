from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.ReadOnlyField(source='post.id')
    
    class Meta:
        model = Comment
        fields = ['id','owner','post','text','created_at']
        
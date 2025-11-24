from rest_framework import serializers
from .models import Post,Like
from comments.serializers import CommentSerializer



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # owner is read-onlt (can't be changed by the user)
    people_who_liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','owner','title','content','created_at','likes_count','people_who_liked','comments_count','comments']

    def get_likes_count(self,obj):
        return obj.likes.count()    
    
    def get_comments_count(self,obj):
        return obj.comments.count()


    def get_people_who_liked(self,obj):
        people = [like.user.username for like in obj.likes.all()]
        return people


class LikeSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Like
        fields = ['id','user','post']
        read_only_fields = ['user','post']
from rest_framework import serializers
from .models import Profile, Follow
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): # User Registration API
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
        )   
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Profile
        fields = ['id','user','bio','image']


class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    following = serializers.ReadOnlyField(source='following.username')
    class Meta:
        model = Follow
        fields = ['id','follower','following','created_at']
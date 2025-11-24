from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import UserSerializer,ProfileSerializer,FollowSerializer
from .models import Profile, Follow
from django.contrib.auth.models import User
from .permissions import IsProfileOwnerOrReadOnly

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]

class MyProfile(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrReadOnly]
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class FollowCreateView(generics.CreateAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        following_username = self.kwargs['username']
        following_user = User.objects.get(username=following_username)
        serializer.save(follower=self.request.user,following=following_user)


class UnFollowView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        follower = self.request.user
        following_username = self.kwargs['username']
        return Follow.objects.get(follower=follower,following__username=following_username)

class FollowersList(generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Follow.objects.filter(following__username=username)


class FollowingList(generics.ListAPIView):
    serializer_class = FollowSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Follow.objects.filter(follower__username=username)
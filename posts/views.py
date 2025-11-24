from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,permissions,status
from .serializers import PostSerializer,LikeSerializer
from .models import Post,Like
from .permissions import IsPostOwner
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend #type:ignore
from rest_framework.filters import OrderingFilter,SearchFilter

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at').select_related('owner').prefetch_related('comments') # optimization queryset (3SQl queries --> 1SQL query)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    #filterset_class = PostFilter
    search_fields = ['title','content','owner__username']
    ordering_fields = ['created_at']
    ordering = ['-created_at']
    


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostOwner]


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,post_id):
        post = Post.objects.get(id=post_id)

        #Check if already liked
        if Like.objects.filter(user=request.user,post=post).exists():
            return Response({"detail":"Post is already Liked!"},status=201)
        
        Like.objects.create(user=request.user,post=post)
        return Response({'detail':'post liked!'},status=201)
    
class UnLikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,post_id):
        post = Post.objects.get(id=post_id)
        like = Like.objects.filter(user=request.user,post=post).first()
        if not like:
            return Response({"detail":"You didn't like this post"},status=400) 
        like.delete()
        return Response({"detail":"unliked the post"},status=201)   



class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.values_list('following_id',flat=True)
        return (Post.objects.filter(owner_id__in=following_users).select_related('owner').order_by('-created_at'))

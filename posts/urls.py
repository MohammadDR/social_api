from django.urls import path
from . import views

urlpatterns = [
    path('',views.PostListCreateView.as_view(),name='post-list'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('<int:post_id>/like/',views.LikePostView.as_view(),name='like-post'),
    path('<int:post_id>/unlike/',views.UnLikePostView.as_view(),name='unlike-post'),
    path('feed/',views.FeedView.as_view(),name='feed')
]
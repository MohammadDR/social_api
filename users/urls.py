from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'), # create user
    path('profile/<int:pk>/',views.ProfileDetailView.as_view(),name='profile'),
    path('profile/me/',views.MyProfile.as_view(),name='my-profile'),
    path('<str:username>/follow/',views.FollowCreateView.as_view(),name='follow'),
    path('<str:username>/unfollow/',views.UnFollowView.as_view(),name='unfollow'),
    path('<str:username>/followers/',views.FollowersList.as_view(),name='followers'),
    path('<str:username>/following/',views.FollowingList.as_view(),name='following'),
]
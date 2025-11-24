from django.urls import path
from . import views

urlpatterns = [
    path('',views.NotificationListView.as_view()),
    path('<int:pk>/mark_read/',views.NotificationMarkReadView.as_view())
]
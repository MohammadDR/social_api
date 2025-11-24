from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    receiver = serializers.ReadOnlyField(source='receiver.username')
    post = serializers.ReadOnlyField(source='post.title')
    comment = serializers.ReadOnlyField(source='comment.id')
    class Meta:
        model = Notification
        fields = '__all__'
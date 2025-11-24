from django.db import models
from django.contrib.auth.models import User
from users.models import Follow
from comments.models import Comment
from posts.models import Like,Post


class Notification(models.Model):
    NOTIFICATION_TYPRS = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
    )

    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent_notifications')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')
    notification_type = models.CharField(max_length=50,choices=NOTIFICATION_TYPRS)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User
from posts.models import Post # type:ignore

class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"comment by {self.owner.username} on {self.post.title}"

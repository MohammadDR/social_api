from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='profiles/',default='default.png')
    def __str__(self):
        return self.user.username


class Follow(models.Model):
    follower = models.ForeignKey(User,related_name='following',on_delete=models.CASCADE)
    following = models.ForeignKey(User,related_name='followers',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('follower','following') # prevents duplicate follow records

    def __str__(self):
        return f"{self.follower} starts following {self.following}"
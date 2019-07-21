from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Contents = models.TextField()
    Created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title

# comment
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Writer = models.CharField(max_length=100)
    Contents = models.TextField()
    Created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title

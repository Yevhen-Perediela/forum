from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)

class Articles(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def __str__(self):
        return self.title

class Comments(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text
from django.db import models
from django.conf import settings
from authentication.models import User


# Create your models here
class UserPost(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.TextField(max_length=256, blank=True, null=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_unlike", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']


class Comment(models.Model):
    comment = models.TextField(max_length=256, blank=True, null=True)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, null=True, blank=True)
    comment_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment_by",
                                   null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

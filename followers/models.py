from django.db import models
from django.conf import settings
import uuid

# Create your models here.

class Follower(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,related_name='user_to_follow')
    followed_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followed_by')
    requested_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='requested_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return


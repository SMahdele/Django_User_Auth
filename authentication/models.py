from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from .managers import UserManager
import uuid



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''
        #refresh = RefreshToken.for_user(self)
        #return {
            #'refresh': str(refresh),
            #'access': str(refresh.access_token)
        #}

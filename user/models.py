from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import *

# Create your models here.
class UserProject(models.Model):
    title= models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_date= models.DateTimeField(default=datetime.now)
    end_date= models.DateTimeField(default=datetime.now)
    description= models.CharField(max_length=256)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return ''


class UserExperience(models.Model):
    company_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=100)
    start_date=models.DateTimeField(default=datetime.now)
    end_date=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return ''


class UserEducation(models.Model):
    degree=models.CharField(max_length=100)
    start_date=models.DateTimeField(default=datetime.now)
    end_date=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return ''


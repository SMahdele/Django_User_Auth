# Generated by Django 3.1.7 on 2021-04-05 12:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0006_delete_likedislike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='userpost',
            name='like',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userpost',
            name='likes_by',
            field=models.ManyToManyField(blank=True, related_name='like_unlike', to=settings.AUTH_USER_MODEL),
        ),
    ]

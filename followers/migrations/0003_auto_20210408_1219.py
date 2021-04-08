# Generated by Django 3.1.7 on 2021-04-08 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0002_auto_20210408_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to_follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
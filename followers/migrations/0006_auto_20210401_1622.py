# Generated by Django 3.1.7 on 2021-04-01 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0005_auto_20210401_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='user_to_follow',
            new_name='user',
        ),
    ]

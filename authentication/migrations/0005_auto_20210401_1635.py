# Generated by Django 3.1.7 on 2021-04-01 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20210401_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_used',
            new_name='is_private',
        ),
    ]

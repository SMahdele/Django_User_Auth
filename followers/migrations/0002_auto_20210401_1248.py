# Generated by Django 3.1.7 on 2021-04-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
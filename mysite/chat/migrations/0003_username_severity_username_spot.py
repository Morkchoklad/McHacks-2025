# Generated by Django 5.1.5 on 2025-01-26 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='username',
            name='severity',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='username',
            name='spot',
            field=models.IntegerField(default=0),
        ),
    ]

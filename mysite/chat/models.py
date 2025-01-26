from django.db import models

class Queue(models.Model):
    hospital = models.CharField(max_length=30)
    blue = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    yellow = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    white = models.IntegerField(default=0)

class Username(models.Model):
    username = models.CharField(max_length=50)
    overall_spot = models.IntegerField(default= 0)
    severity = models.IntegerField(default= 5)

class Message(models.Model):
    username = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
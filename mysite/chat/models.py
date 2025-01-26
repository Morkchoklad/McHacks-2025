from django.db import models

class Queue(models.Model):
    hospital = models.CharField(max_length=30)
    blue = models.IntegerField(default=0)
    red = models.IntegerField(default=0)
    yellow = models.IntegerField(default=0)
    green = models.IntegerField(default=0)
    white = models.IntegerField(default=0)


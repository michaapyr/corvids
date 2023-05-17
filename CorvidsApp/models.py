from django.db import models

class Likes(models.Model):
    bird = models.CharField(max_length=250, unique=True)
    likes = models.IntegerField()
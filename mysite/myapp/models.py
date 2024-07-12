from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    rating = models.FloatField()
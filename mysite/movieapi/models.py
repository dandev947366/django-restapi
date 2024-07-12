from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

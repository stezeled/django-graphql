from django.db import models

class Movie(models.Model):
    tittle = models.CharField(max_length=32)
    year = models.IntegerField(default=2000)


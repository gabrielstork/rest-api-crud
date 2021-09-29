from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    country = models.CharField(max_length=100)
    programmer = models.BooleanField()
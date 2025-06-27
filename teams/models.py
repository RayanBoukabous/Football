from django.db import models
from countrys.models import *


class Team(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    established_year = models.IntegerField()
    flag = models.ImageField(upload_to="flags/", null=True, blank=True)

    def __str__(self):
        return self.name

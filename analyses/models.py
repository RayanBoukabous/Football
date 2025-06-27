from django.db import models
from teams.models import *
from matches.models import *


class Analyse(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, null=True, blank=True, on_delete=models.CASCADE)
    video = models.FileField(upload_to="analyses/")

    def __str__(self):
        return f"Analyse {self.id}"

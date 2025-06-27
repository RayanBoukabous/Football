from django.db import models
from players.models import *
from teams.models import *
from matches.models import *


class Individuality(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    player = models.ForeignKey(Player, null=True, blank=True, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, null=True, blank=True, on_delete=models.CASCADE)
    video = models.FileField(upload_to="individual_videos/")

    def __str__(self):
        return f"Individuality {self.id}"

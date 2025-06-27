from django.db import models
from categorys.models import *
from countrys.models import *
from teams.models import *


class Match(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    first = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="first_team_matches"
    )
    second = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="second_team_matches"
    )
    finale_result = models.CharField(max_length=5, null=True, blank=True)
    location = models.ForeignKey(Country, on_delete=models.CASCADE)
    video = models.FileField(upload_to="media/match_videos/")

    def __str__(self):
        return f"Match on {self.match_date} at {self.location}"

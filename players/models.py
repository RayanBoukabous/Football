from django.db import models
from categorys.models import *
from countrys.models import Country
from teams.models import Team
from postes.models import Position


FOOT_CHOICES = [
    ("Droit", "Droit"),
    ("Gauche", "Gauche"),
]


class Player(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    birthdate = models.DateField()
    positions = models.ManyToManyField(Position, blank=False)
    photo = models.ImageField(upload_to="player_photos/", blank=True, null=True)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    strong_feet = models.CharField(
        max_length=10, choices=FOOT_CHOICES, blank=False, null=False
    )
    weak_feet = models.CharField(
        max_length=10, choices=FOOT_CHOICES, blank=True, null=True
    )
    strengths = models.TextField(blank=True, null=True)
    weaknesses = models.TextField(blank=True, null=True)
    club = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

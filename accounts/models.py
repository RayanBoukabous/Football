# users/models.py
from django.db import models
from django.contrib.auth.models import User
from categorys.models import Category


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_of_birth = models.DateField(null=True, blank=True)
    country_of_birth = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True, blank=True)
    strong_foot = models.CharField(max_length=50, null=True, blank=True)
    weak_foot = models.CharField(max_length=50, null=True, blank=True)
    observations = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

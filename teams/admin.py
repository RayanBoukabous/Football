from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "established_year")
    search_fields = ("name", "country__name")
    list_filter = ("country",)


admin.site.register(Team, TeamAdmin)

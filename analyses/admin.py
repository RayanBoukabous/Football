from django.contrib import admin
from .models import Analyse


# Register your models here.


class AnalyseAdmin(admin.ModelAdmin):
    list_display = ("id", "team", "match", "video")


admin.site.register(Analyse, AnalyseAdmin)

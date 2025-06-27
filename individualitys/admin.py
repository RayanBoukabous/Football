from django.contrib import admin
from .models import Individuality


# Register your models here.


class IndividualityAdmin(admin.ModelAdmin):
    list_display = ("player", "team", "match", "video")
    search_fields = ("player__name", "team__name", "match__date")
    list_filter = ("player", "team", "match")


admin.site.register(Individuality, IndividualityAdmin)

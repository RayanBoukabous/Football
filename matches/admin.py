from django.contrib import admin
from .models import Match


# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ("match_date", "category", "video")
    search_fields = ("category__name",)
    list_filter = ("category",)


admin.site.register(Match, MatchAdmin)

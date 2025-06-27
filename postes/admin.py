from django.contrib import admin
from .models import Position


# Register your models here.


class PositionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Position, PositionAdmin)

from django.contrib import admin
from .models import Country


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(Country, CountryAdmin)

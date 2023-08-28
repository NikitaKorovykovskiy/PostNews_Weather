from .models import WeatherSummary
from django.contrib import admin


class WeatherAdmin(admin.ModelAdmin):
    list_display = ("sight", "humidity", "pressure")


admin.site.register(WeatherSummary, WeatherAdmin)

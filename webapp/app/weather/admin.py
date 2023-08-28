from django.contrib import admin

from .models import WeatherSummary


class WeatherAdmin(admin.ModelAdmin):
    list_display = ("sight", "humidity", "pressure")


admin.site.register(WeatherSummary, WeatherAdmin)

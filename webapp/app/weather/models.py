from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from sights.models import Sights


class WeatherSummary(models.Model):
    """
    Модель Сводки погоды
    """

    sight = models.ForeignKey(
        Sights,
        on_delete=models.CASCADE,
        verbose_name="Примечательное место",
    )
    timestamp = models.DateTimeField(verbose_name="Дата")
    temperature = models.IntegerField(
        validators=[MinValueValidator(-100), MaxValueValidator(100)],
        verbose_name="Температура (°C)",
    )
    humidity = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)], verbose_name="Влажность (%)"
    )
    pressure = models.PositiveIntegerField(
        validators=[MinValueValidator(700), MaxValueValidator(800)],
        verbose_name="Атмосферное давление (мм.рт.ст.)",
    )
    wind_direction = models.CharField(
        max_length=5, verbose_name="Направление ветра"
    )
    wind_speed = models.FloatField(
        validators=[MinValueValidator(0)],
        verbose_name="Скорость ветра (м/с)",
    )

    def __str__(self):
        return (
            f'{self.sight.title} - {self.timestamp.strftime("%d-%m-%Y")}'
        )

    class Meta:
        verbose_name = "Сводка погоды"
        verbose_name_plural = "Сводки погоды"

    def get_wind_direction_display(self):
        return "test"

    def serialize(self):
        return {
            "sight": self.sight.title,
            "timestamp": self.timestamp.strftime("%d-%m-%Y"),
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "wind_direction": self.wind_direction,
            "wind_speed": self.wind_speed,
        }

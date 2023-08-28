from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Sights(models.Model):
    title = models.CharField("Название", max_length=50)
    rating = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(25)]
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
    )
    latitude = models.FloatField(
        verbose_name="Широта",
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
    )

    class Meta:
        verbose_name = "Примечательное место"
        verbose_name_plural = "Примечательные места"

    def save(self, *args, **kwargs):
        self.latitude = round(self.latitude, 8)
        self.longitude = round(self.longitude, 8)
        self.latitude = float(f"{self.latitude:.8f}")
        self.longitude = float(f"{self.longitude:.8f}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

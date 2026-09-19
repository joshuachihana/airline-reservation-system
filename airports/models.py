from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=150)
    iata_code = models.CharField(
        max_length=3,
        unique=True
    )
    icao_code = models.CharField(
        max_length=4,
        unique=True
    )
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.iata_code})"
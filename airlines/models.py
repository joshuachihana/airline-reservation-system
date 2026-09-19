from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=100)
    iata_code = models.CharField(
        max_length=2,
        unique=True
    )
    icao_code = models.CharField(
        max_length=3,
        unique=True
    )
    country = models.CharField(max_length=100)
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    email = models.EmailField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
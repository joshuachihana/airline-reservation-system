from django.db import models
from airlines.models import Airline


class Aircraft(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("MAINTENANCE", "Maintenance"),
        ("RETIRED", "Retired"),
    ]

    airline = models.ForeignKey(
        Airline,
        on_delete=models.CASCADE,
        related_name="aircraft"
    )
    registration_number = models.CharField(
        max_length=20,
        unique=True
    )
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.registration_number} - {self.model}"


class Seat(models.Model):
    CLASS_CHOICES = [
        ("ECONOMY", "Economy"),
        ("BUSINESS", "Business"),
        ("FIRST", "First"),
    ]

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.CASCADE,
        related_name="seats"
    )
    seat_number = models.CharField(max_length=5)
    seat_class = models.CharField(
        max_length=20,
        choices=CLASS_CHOICES,
        default="ECONOMY"
    )
    is_exit_row = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["aircraft", "seat_number"],
                name="unique_seat_per_aircraft"
            )
        ]

    def __str__(self):
        return f"{self.aircraft.registration_number} - {self.seat_number}"
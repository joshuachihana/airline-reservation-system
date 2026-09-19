from django.db import models

from airlines.models import Airline
from airports.models import Airport
from aircraft.models import Aircraft


class Flight(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    airline = models.ForeignKey(
        Airline,
        on_delete=models.PROTECT,
        related_name="flights"
    )

    flight_number = models.CharField(
        max_length=10
    )

    origin_airport = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name="departing_flights"
    )

    destination_airport = models.ForeignKey(
        Airport,
        on_delete=models.PROTECT,
        related_name="arriving_flights"
    )

    duration = models.DurationField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "airline",
                    "flight_number",
                    "origin_airport",
                    "destination_airport",
                ],
                name="unique_airline_flight_route"
            )
        ]

    def __str__(self):
        return f"{self.airline.iata_code}{self.flight_number}"


class FlightInstance(models.Model):
    STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("BOARDING", "Boarding"),
        ("DEPARTED", "Departed"),
        ("ARRIVED", "Arrived"),
        ("DELAYED", "Delayed"),
        ("CANCELLED", "Cancelled"),
    ]

    flight = models.ForeignKey(
        Flight,
        on_delete=models.PROTECT,
        related_name="instances"
    )

    aircraft = models.ForeignKey(
        Aircraft,
        on_delete=models.PROTECT,
        related_name="flight_instances"
    )

    departure_datetime = models.DateTimeField()

    arrival_datetime = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="SCHEDULED"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "flight",
                    "departure_datetime"
                ],
                name="unique_flight_instance"
            )
        ]

    def __str__(self):
        return f"{self.flight} - {self.departure_datetime}"
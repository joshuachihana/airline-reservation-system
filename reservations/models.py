from django.db import models

from customers.models import Customer
from flights.models import FlightInstance
from passengers.models import Passenger


class Reservation(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("CANCELLED", "Cancelled"),
        ("COMPLETED", "Completed"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    flight_instance = models.ForeignKey(
        FlightInstance,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    booking_reference = models.CharField(
        max_length=10,
        unique=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.booking_reference


class ReservationPassenger(models.Model):
    PASSENGER_TYPE_CHOICES = [
        ("ADULT", "Adult"),
        ("CHILD", "Child"),
        ("INFANT", "Infant"),
    ]

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name="passengers"
    )

    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    passenger_type = models.CharField(
        max_length=10,
        choices=PASSENGER_TYPE_CHOICES,
        default="ADULT"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["reservation", "passenger"],
                name="unique_passenger_per_reservation"
            )
        ]

    def __str__(self):
        return (
            f"{self.reservation.booking_reference} "
            f"- {self.passenger}"
        )
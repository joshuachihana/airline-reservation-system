from django.db import models

from passengers.models import Passenger
from reservations.models import Reservation
from aircraft.models import Seat


class Ticket(models.Model):
    STATUS_CHOICES = [
        ("ISSUED", "Issued"),
        ("USED", "Used"),
        ("CANCELLED", "Cancelled"),
        ("EXPIRED", "Expired"),
    ]

    ticket_number = models.CharField(
        max_length=20,
        unique=True
    )

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.PROTECT,
        related_name="tickets"
    )

    passenger = models.ForeignKey(
        Passenger,
        on_delete=models.PROTECT,
        related_name="tickets"
    )

    seat = models.ForeignKey(
        Seat,
        on_delete=models.PROTECT,
        related_name="tickets"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ISSUED"
    )

    issued_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.ticket_number
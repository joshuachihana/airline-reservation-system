from django.db import models

from reservations.models import Reservation


class Payment(models.Model):
    METHOD_CHOICES = [
        ("CASH", "Cash"),
        ("CARD", "Card"),
        ("MOBILE_MONEY", "Mobile Money"),
        ("BANK_TRANSFER", "Bank Transfer"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
        ("REFUNDED", "Refunded"),
    ]

    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.PROTECT,
        related_name="payments"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=METHOD_CHOICES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    transaction_reference = models.CharField(
        max_length=100,
        unique=True
    )

    paid_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.transaction_reference
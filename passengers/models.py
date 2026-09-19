from django.db import models


class Passenger(models.Model):
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    nationality = models.CharField(
        max_length=100
    )

    passport_number = models.CharField(
        max_length=50,
        unique=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
import random
import string

from rest_framework import serializers

from .models import Reservation, ReservationPassenger


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = "__all__"
        read_only_fields = [
            "booking_reference",
        ]

    def create(self, validated_data):

        while True:
            booking_reference = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=10
                )
            )

            if not Reservation.objects.filter(
                booking_reference=booking_reference
            ).exists():
                break

        validated_data["booking_reference"] = booking_reference

        return Reservation.objects.create(
            **validated_data
        )


class ReservationPassengerSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = ReservationPassenger
        fields = "__all__"
from rest_framework import serializers

from .models import Ticket


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = "__all__"

    def validate(self, attrs):
        reservation = attrs.get("reservation")
        passenger = attrs.get("passenger")
        seat = attrs.get("seat")

        # Validate passenger belongs to reservation
        if reservation and passenger:
            if not reservation.passengers.filter(
                passenger=passenger
            ).exists():
                raise serializers.ValidationError({
                    "passenger": (
                        "This passenger does not belong "
                        "to the reservation."
                    )
                })

        # Validate seat belongs to the aircraft
        # assigned to the flight instance
        if reservation and seat:
            flight_instance = reservation.flight_instance

            if seat.aircraft_id != flight_instance.aircraft_id:
                raise serializers.ValidationError({
                    "seat": (
                        "This seat does not belong to "
                        "the aircraft assigned to this flight."
                    )
                })

        return attrs
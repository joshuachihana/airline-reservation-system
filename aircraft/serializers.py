from rest_framework import serializers

from .models import Aircraft, Seat


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = "__all__"


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"
from rest_framework import serializers

from .models import Flight, FlightInstance


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"


class FlightInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightInstance
        fields = "__all__"
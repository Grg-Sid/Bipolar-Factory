from rest_framework import serializers

from .models import Flights, Bookings, Passengers


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = "__all__"


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = "__all__"

from rest_framework import serializers

from .models import Flights, Bookings, Passengers


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = "__all__"


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = ["first_name", "last_name"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = "__all__"

    def to_representation(self, instance):
        data = {
            "id": instance.id,
            "flight": {"flight_number": instance.flight.flight_number},
            "passengers": [
                {"first_name": passenger.first_name}
                for passenger in instance.passengers.all()
            ],
        }
        return data

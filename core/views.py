from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import FlightSerializer, BookingSerializer, PassengerSerializer
from .models import Flights, Bookings, Passengers


class FlightList(APIView):
    def get(self, request):
        flights = Flights.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlightDetail(APIView):
    def get(self, request, pk):
        flight = Flights.objects.get(pk=pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlightCreate(APIView):
    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookFlight(APIView):
    def post(self, request):
        flight_id = request.data.get("flight_id")
        user_id = request.data.get("user_id")
        passengers = request.data.get("passengers")
        flight = Flights.objects.get(pk=flight_id)
        user = "users.CustomUser".objects.get(pk=user_id)
        booking = Bookings.objects.create(flight=flight, user=user)
        booking.passengers.set(passengers)
        booking.save()


class BookingList(APIView):
    def get(self, request):
        bookings = Bookings.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingDetail(APIView):
    def get(self, request, pk):
        booking = Bookings.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)


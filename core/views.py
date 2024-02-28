from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework import status

from .serializers import FlightSerializer, BookingSerializer
from .models import Flights, Bookings, Passengers


class FlightList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        flights = Flights.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlightDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        flight = Flights.objects.get(pk=pk)
        serializer = FlightSerializer(flight)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlightCreate(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookFlight(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        flight_id = request.data.get("flight_id")
        user_id = request.data.get("user_id")
        passengers_data = request.data.get("passengers")

        if not all(
            passenger_data.get("first_name") and passenger_data.get("last_name")
            for passenger_data in passengers_data
        ):
            return Response(
                {"error": "Passenger information is incomplete"}, status=400
            )

        flight = Flights.objects.get(pk=flight_id)
        User = get_user_model()
        user = User.objects.get(pk=user_id)

        passengers = []
        for passenger_data in passengers_data:
            passenger = Passengers(
                first_name=passenger_data["first_name"],
                last_name=passenger_data["last_name"],
            )
            passengers.append(passenger)

        if len(passengers) > flight.no_of_seats:
            return Response(
                {"error": "Not enough seats available"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        with transaction.atomic():
            booking = Bookings.objects.create(flight=flight, user=user)

            Passengers.objects.bulk_create(passengers)

            booking.passengers.set(passengers)

            flight.no_of_seats -= len(passengers)
            flight.save()

        return Response({"message": "Booking created successfully"})


class BookingList(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        if request.user.is_admin:
            bookings = Bookings.objects.all()
        else:
            bookings = Bookings.objects.filter(user=request.user)

        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookingDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        booking = Bookings.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBookings(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        bookings = user.bookings_set.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.urls import path
from .views import (
    FlightList,
    FlightDetail,
    FlightCreate,
    BookFlight,
    BookingList,
    BookingDetail,
    PassengerList,
)

urlpatterns = [
    path("flights/", FlightList.as_view(), name="flight-list"),
    path("flights/<int:pk>/", FlightDetail.as_view(), name="flight-detail"),
    path("flights/create/", FlightCreate.as_view(), name="flight-create"),
    path("book/", BookFlight.as_view(), name="book-flight"),
    path("bookings/", BookingList.as_view(), name="booking-list"),
    path("bookings/<int:pk>/", BookingDetail.as_view(), name="booking-detail"),
    path("passengers/", PassengerList.as_view(), name="passenger-list"),
]

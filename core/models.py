from django.db import models


class Flights(models.Model):
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    duration = models.IntegerField()
    time_of_departure = models.DateTimeField()
    time_of_arrival = models.DateTimeField()
    no_of_seats = models.IntegerField(default=60)

    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"


class Bookings(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    passengers = models.ManyToManyField("Passengers", blank=True)

    def __str__(self):
        return f"{self.flight} - {self.passenger}"


class Passengers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

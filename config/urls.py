from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/airlines/",
        include("airlines.urls")
    ),

    path(
        "api/airports/",
        include("airports.urls")
    ),

    path(
        "api/aircraft/",
        include("aircraft.urls")
    ),

    path(
        "api/flights/",
        include("flights.urls")
    ),

    path(
        "api/customers/",
        include("customers.urls")
    ),

    path(
        "api/passengers/",
        include("passengers.urls")
    ),

    path(
        "api/reservations/",
        include("reservations.urls")
    ),

    path(
        "api/tickets/",
        include("tickets.urls")
        ),

    path("api/payments/", include("payments.urls")),

]
from django.urls import path

from .views import (
    FlightListCreateAPIView,
    FlightDetailAPIView
)


urlpatterns = [
    path(
        "",
        FlightListCreateAPIView.as_view(),
        name="flight-list-create"
    ),

    path(
        "<int:pk>/",
        FlightDetailAPIView.as_view(),
        name="flight-detail"
    ),
]
from django.urls import path

from .views import (
    AircraftListCreateAPIView,
    AircraftDetailAPIView,
    SeatListCreateAPIView,
    SeatDetailAPIView
)


urlpatterns = [
    path(
        "",
        AircraftListCreateAPIView.as_view(),
        name="aircraft-list-create"
    ),

    path(
        "<int:pk>/",
        AircraftDetailAPIView.as_view(),
        name="aircraft-detail"
    ),

    path(
        "seats/",
        SeatListCreateAPIView.as_view(),
        name="seat-list-create"
    ),

    path(
        "seats/<int:pk>/",
        SeatDetailAPIView.as_view(),
        name="seat-detail"
    ),
]
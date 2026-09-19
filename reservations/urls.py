from django.urls import path

from .views import (
    ReservationListCreateAPIView,
    ReservationDetailAPIView,
    ReservationPassengerListCreateAPIView,
    ReservationPassengerDetailAPIView
)


urlpatterns = [
    path(
        "",
        ReservationListCreateAPIView.as_view(),
        name="reservation-list-create"
    ),

    path(
        "passengers/",
        ReservationPassengerListCreateAPIView.as_view(),
        name="reservation-passenger-list-create"
    ),

    path(
        "passengers/<int:pk>/",
        ReservationPassengerDetailAPIView.as_view(),
        name="reservation-passenger-detail"
    ),

    path(
        "<int:pk>/",
        ReservationDetailAPIView.as_view(),
        name="reservation-detail"
    ),
]
from django.urls import path

from .views import (
    PassengerListCreateAPIView,
    PassengerDetailAPIView
)


urlpatterns = [
    path(
        "",
        PassengerListCreateAPIView.as_view(),
        name="passenger-list-create"
    ),

    path(
        "<int:pk>/",
        PassengerDetailAPIView.as_view(),
        name="passenger-detail"
    ),
]
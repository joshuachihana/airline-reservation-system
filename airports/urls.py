from django.urls import path

from .views import (
    AirportListCreateAPIView,
    AirportDetailAPIView
)


urlpatterns = [
    path(
        "",
        AirportListCreateAPIView.as_view(),
        name="airport-list-create"
    ),

    path(
        "<int:pk>/",
        AirportDetailAPIView.as_view(),
        name="airport-detail"
    ),
]
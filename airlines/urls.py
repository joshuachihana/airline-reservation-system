from django.urls import path

from .views import (
    AirlineListCreateAPIView,
    AirlineDetailAPIView
)


urlpatterns = [
    path(
        "",
        AirlineListCreateAPIView.as_view(),
        name="airline-list-create"
    ),

    path(
        "<int:pk>/",
        AirlineDetailAPIView.as_view(),
        name="airline-detail"
    ),
]
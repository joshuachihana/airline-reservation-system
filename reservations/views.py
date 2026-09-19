from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Reservation, ReservationPassenger

from .serializers import (
    ReservationSerializer,
    ReservationPassengerSerializer
)


class ReservationListCreateAPIView(APIView):

    def get(self, request):
        reservations = Reservation.objects.all()

        serializer = ReservationSerializer(
            reservations,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ReservationDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Reservation.objects.get(pk=pk)

        except Reservation.DoesNotExist:
            return None

    def get(self, request, pk):
        reservation = self.get_object(pk)

        if reservation is None:
            return Response(
                {"detail": "Reservation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationSerializer(reservation)

        return Response(serializer.data)

    def put(self, request, pk):
        reservation = self.get_object(pk)

        if reservation is None:
            return Response(
                {"detail": "Reservation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationSerializer(
            reservation,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        reservation = self.get_object(pk)

        if reservation is None:
            return Response(
                {"detail": "Reservation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationSerializer(
            reservation,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        reservation = self.get_object(pk)

        if reservation is None:
            return Response(
                {"detail": "Reservation not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        reservation.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class ReservationPassengerListCreateAPIView(APIView):

    def get(self, request):
        reservation_passengers = (
            ReservationPassenger.objects.all()
        )

        serializer = ReservationPassengerSerializer(
            reservation_passengers,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationPassengerSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ReservationPassengerDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return ReservationPassenger.objects.get(pk=pk)

        except ReservationPassenger.DoesNotExist:
            return None

    def get(self, request, pk):
        reservation_passenger = self.get_object(pk)

        if reservation_passenger is None:
            return Response(
                {"detail": "Reservation passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationPassengerSerializer(
            reservation_passenger
        )

        return Response(serializer.data)

    def put(self, request, pk):
        reservation_passenger = self.get_object(pk)

        if reservation_passenger is None:
            return Response(
                {"detail": "Reservation passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationPassengerSerializer(
            reservation_passenger,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        reservation_passenger = self.get_object(pk)

        if reservation_passenger is None:
            return Response(
                {"detail": "Reservation passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = ReservationPassengerSerializer(
            reservation_passenger,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        reservation_passenger = self.get_object(pk)

        if reservation_passenger is None:
            return Response(
                {"detail": "Reservation passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        reservation_passenger.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Passenger
from .serializers import PassengerSerializer


class PassengerListCreateAPIView(APIView):

    def get(self, request):
        passengers = Passenger.objects.all()

        serializer = PassengerSerializer(
            passengers,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = PassengerSerializer(
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


class PassengerDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Passenger.objects.get(pk=pk)

        except Passenger.DoesNotExist:
            return None

    def get(self, request, pk):
        passenger = self.get_object(pk)

        if passenger is None:
            return Response(
                {"detail": "Passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PassengerSerializer(passenger)

        return Response(serializer.data)

    def put(self, request, pk):
        passenger = self.get_object(pk)

        if passenger is None:
            return Response(
                {"detail": "Passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PassengerSerializer(
            passenger,
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
        passenger = self.get_object(pk)

        if passenger is None:
            return Response(
                {"detail": "Passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PassengerSerializer(
            passenger,
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
        passenger = self.get_object(pk)

        if passenger is None:
            return Response(
                {"detail": "Passenger not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        passenger.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Flight, FlightInstance
from .serializers import (
    FlightSerializer,
    FlightInstanceSerializer
)


class FlightListCreateAPIView(APIView):

    def get(self, request):
        flights = Flight.objects.all()

        serializer = FlightSerializer(
            flights,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = FlightSerializer(
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


class FlightDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Flight.objects.get(pk=pk)

        except Flight.DoesNotExist:
            return None

    def get(self, request, pk):
        flight = self.get_object(pk)

        if flight is None:
            return Response(
                {"detail": "Flight not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightSerializer(flight)

        return Response(serializer.data)

    def put(self, request, pk):
        flight = self.get_object(pk)

        if flight is None:
            return Response(
                {"detail": "Flight not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightSerializer(
            flight,
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
        flight = self.get_object(pk)

        if flight is None:
            return Response(
                {"detail": "Flight not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightSerializer(
            flight,
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
        flight = self.get_object(pk)

        if flight is None:
            return Response(
                {"detail": "Flight not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        flight.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class FlightInstanceListCreateAPIView(APIView):

    def get(self, request):
        instances = FlightInstance.objects.all()

        serializer = FlightInstanceSerializer(
            instances,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = FlightInstanceSerializer(
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


class FlightInstanceDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return FlightInstance.objects.get(pk=pk)

        except FlightInstance.DoesNotExist:
            return None

    def get(self, request, pk):
        instance = self.get_object(pk)

        if instance is None:
            return Response(
                {"detail": "Flight instance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightInstanceSerializer(instance)

        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)

        if instance is None:
            return Response(
                {"detail": "Flight instance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightInstanceSerializer(
            instance,
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
        instance = self.get_object(pk)

        if instance is None:
            return Response(
                {"detail": "Flight instance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = FlightInstanceSerializer(
            instance,
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
        instance = self.get_object(pk)

        if instance is None:
            return Response(
                {"detail": "Flight instance not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        instance.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
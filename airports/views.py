from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Airport
from .serializers import AirportSerializer


class AirportListCreateAPIView(APIView):

    def get(self, request):
        airports = Airport.objects.all()

        serializer = AirportSerializer(
            airports,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AirportSerializer(
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


class AirportDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Airport.objects.get(pk=pk)

        except Airport.DoesNotExist:
            return None

    def get(self, request, pk):
        airport = self.get_object(pk)

        if airport is None:
            return Response(
                {"detail": "Airport not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AirportSerializer(airport)

        return Response(serializer.data)

    def put(self, request, pk):
        airport = self.get_object(pk)

        if airport is None:
            return Response(
                {"detail": "Airport not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AirportSerializer(
            airport,
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
        airport = self.get_object(pk)

        if airport is None:
            return Response(
                {"detail": "Airport not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AirportSerializer(
            airport,
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
        airport = self.get_object(pk)

        if airport is None:
            return Response(
                {"detail": "Airport not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        airport.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Aircraft
from .serializers import AircraftSerializer


class AircraftListCreateAPIView(APIView):

    def get(self, request):
        aircraft = Aircraft.objects.all()

        serializer = AircraftSerializer(
            aircraft,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = AircraftSerializer(
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


class AircraftDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Aircraft.objects.get(pk=pk)

        except Aircraft.DoesNotExist:
            return None

    def get(self, request, pk):
        aircraft = self.get_object(pk)

        if aircraft is None:
            return Response(
                {"detail": "Aircraft not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AircraftSerializer(aircraft)

        return Response(serializer.data)

    def put(self, request, pk):
        aircraft = self.get_object(pk)

        if aircraft is None:
            return Response(
                {"detail": "Aircraft not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AircraftSerializer(
            aircraft,
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
        aircraft = self.get_object(pk)

        if aircraft is None:
            return Response(
                {"detail": "Aircraft not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AircraftSerializer(
            aircraft,
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
        aircraft = self.get_object(pk)

        if aircraft is None:
            return Response(
                {"detail": "Aircraft not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        aircraft.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class SeatListCreateAPIView(APIView):

    def get(self, request):
        seats = Seat.objects.all()

        serializer = SeatSerializer(
            seats,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):
        serializer = SeatSerializer(
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


class SeatDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Seat.objects.get(pk=pk)

        except Seat.DoesNotExist:
            return None

    def get(self, request, pk):
        seat = self.get_object(pk)

        if seat is None:
            return Response(
                {"detail": "Seat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SeatSerializer(seat)

        return Response(serializer.data)

    def put(self, request, pk):
        seat = self.get_object(pk)

        if seat is None:
            return Response(
                {"detail": "Seat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SeatSerializer(
            seat,
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
        seat = self.get_object(pk)

        if seat is None:
            return Response(
                {"detail": "Seat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = SeatSerializer(
            seat,
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
        seat = self.get_object(pk)

        if seat is None:
            return Response(
                {"detail": "Seat not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        seat.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
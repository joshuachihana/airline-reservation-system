from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Payment
from .serializers import PaymentSerializer


class PaymentListCreateAPIView(APIView):

    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)

        if serializer.is_valid():
            payment = serializer.save()

            return Response(
                PaymentSerializer(payment).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PaymentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Payment.objects.get(pk=pk)
        except Payment.DoesNotExist:
            return None

    def get(self, request, pk):
        payment = self.get_object(pk)

        if payment is None:
            return Response(
                {"detail": "Payment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentSerializer(payment)

        return Response(serializer.data)

    def put(self, request, pk):
        payment = self.get_object(pk)

        if payment is None:
            return Response(
                {"detail": "Payment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentSerializer(
            payment,
            data=request.data
        )

        if serializer.is_valid():
            payment = serializer.save()

            return Response(
                PaymentSerializer(payment).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        payment = self.get_object(pk)

        if payment is None:
            return Response(
                {"detail": "Payment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PaymentSerializer(
            payment,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            payment = serializer.save()

            return Response(
                PaymentSerializer(payment).data
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        payment = self.get_object(pk)

        if payment is None:
            return Response(
                {"detail": "Payment not found."},
                status=status.HTTP_404_NOT_FOUND
            )

        payment.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
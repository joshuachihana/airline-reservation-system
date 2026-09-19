from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def validate(self, attrs):
        amount = attrs.get("amount")

        if amount is not None and amount <= 0:
            raise serializers.ValidationError({
                "amount": "Payment amount must be greater than zero."
            })

        return attrs
from rest_framework import serializers
from .models import CartItem


class CarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

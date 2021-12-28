from rest_framework import serializers

from apps.orders.models import Order, ProductOrder


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ("id", "title", "quantity", "price")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "cart",
            "user",
            "address",
            "last_name",
            "first_name",
            "email",
            "phone_number",
            "comment",
            "payment_type",
            "total_sum",
        )
        read_only_fields = ("cart", "user", "total_sum")


class OrderDetailSerializer(serializers.ModelSerializer):
    product_order_order = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "cart",
            "user",
            "address",
            "last_name",
            "first_name",
            "email",
            "phone_number",
            "comment",
            "payment_type",
            "total_sum",
            "product_order_order",
        )
        read_only_fields = ("cart", "user", "total_sum")


class OrderDetailSerializer(serializers.ModelSerializer):
    order_product = ProductOrderSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id', 'cart', 'user', 'address', 'last_name',
            'first_name', 'email', 'phone_number',
            'comment', 'payment_type', 'total_sum',
            'order_product'
        )
        read_only_fields = (
            'cart', 'user', 'total_sum'
        )

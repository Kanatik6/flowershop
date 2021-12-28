from rest_framework import serializers

from apps.carts import models
from apps.products.serializers import ProductItemSerializers
from rest_framework.serializers import ReadOnlyField


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ("id", "product", "amount" )
        read_only_fields = ["total_sum"]

    def create(self, validated_data):
        amount = validated_data.get('amount')
        cart_item = models.CartItem.objects.create(
            product=validated_data.get("product"),
            amount=amount,
            total_sum=0,
            cart=validated_data.get("cart"),
        )
        cart_item.save()
        cart_item.total_sum = cart_item.get_total_price()
        cart_item.save()

        if cart_item:
            total = cart_item.total_sum
            user = self.context['request'].user
            user = 1
            cart = models.Cart.objects.get(user=user)
            cart.total_sum = cart.get_total_quantity_price
            cart.save()

        return cart_item


class CartItemDetailSerializers(serializers.ModelSerializer):
    product = ProductItemSerializers(read_only=True)

    class Meta:
        model = models.CartItem
        fields = ("id", "product", "amount", "total_sum")
        read_only_fields = ["total_sum"]


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemDetailSerializers(many=True, read_only=True)

    class Meta:
        model = models.Cart
        fields = ("id", "user", "cart_items", "total_sum")

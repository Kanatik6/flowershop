from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.carts.models import Cart, CartItem
from apps.carts.serializers import CartSerializer, CartItemSerializer, CartItemDetailSerializers
from apps.products.models import ProductItem


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Cart.objects.get_or_new(request)
        serializer = CartSerializer(queryset, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemDetailSerializers


class CartItemCreate(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.get_or_new(request)
        cart_item = cart.cart_items.all()
        product = ProductItem.objects.get(pk=request.data["product"])

        for item in cart_item:
            if item.product == product:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if int(request.data["amount"]) > product.quantity:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        cart = Cart.objects.get_or_new(self.request)
        return serializer.save(cart=cart)

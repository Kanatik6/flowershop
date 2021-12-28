from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.favorites.models import Favorite
from apps.favorites.serializers import (
    FavoriteListSerializer, FavoriteAddSerializer
)
from apps.products.models import ProductItem


class FavoriteViewSet(viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer

    @swagger_auto_schema(
        responses={200: FavoriteListSerializer()}, request_body=FavoriteAddSerializer
    )
    @action(detail=True, methods=["put"])
    def add_or_remove_favorite(self, request, pk=None):
        serializer = FavoriteAddSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product_to_add = ProductItem.objects.filter(id=request.data['product_id']).first()
            favorite_obj = self.get_object()
            if favorite_obj.user != request.user:
                return Response('You cannot modify the favorite object.')

            if favorite_obj.products.filter(id=product_to_add.id).exists():
                favorite_obj.products.remove(product_to_add)
                favorite_obj.save()
                return Response(data=FavoriteListSerializer(favorite_obj).data)

            favorite_obj.products.add(product_to_add)
            favorite_obj.save()
            return Response(data=FavoriteListSerializer(favorite_obj).data)

    @swagger_auto_schema(responses={200: FavoriteListSerializer()})
    @action(detail=False, methods=["get"])
    def get_my_favorites(self, request):
        user = request.user
        if user.is_authenticated:
            users_favs = Favorite.objects.filter(user=user)
            return Response(FavoriteListSerializer(users_favs, many=True).data)
        return Response({'User is not authenticated'})

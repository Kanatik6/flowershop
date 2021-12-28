from rest_framework import serializers

from apps.favorites.models import Favorite
from apps.products.serializers import ProductItemSerializers
from apps.products.models import ProductItem
from apps.products.serializers import ProductSerializers
from apps.users.models import User


class FavoriteListSerializer(serializers.ModelSerializer):
    products = ProductItemSerializers(many=True)

    class Meta:
        model = Favorite
        fields = (
            "id",
            "products",
            "user",
        )


class FavoriteAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()

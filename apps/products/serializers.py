from rest_framework import serializers

from apps.products.models import Product, ProductImage, ProductItem


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "article")


class ProductItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = (
            "id",
            "title",
            "size",
            "category",
            "product",
            "description",
            "equipment",
            "is_new",
            "bouquet_care",
            "specifications",
            "discount",
        )


class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image", "product_id")

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import viewsets, views
from apps.favorites.models import Favorite
from django.contrib.auth import get_user_model

from apps.products.models import Product, ProductItem, ProductImage
from apps.products.serializers import (
    ProductSerializers,
    ProductItemSerializers,
    ProductImageSerializers,
)

User = get_user_model()


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["article"]
    ordering_fields = ["article"]


class ProductItemAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filter_fields = ["category", "is_new"]
    search_fields = [
        "title",
        "size",
        "discount",
        "description",
        "equipment",
        "bouquet_care",
        "specifications",
        "discount",
    ]

    ordering_fields = [
        "title",
        "size",
        "discount",
        "description",
        "equipment",
        "bouquet_care",
        "specifications",
        "discount",
    ]


class ProductImageAPIViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializers


class RecommendationListView(views.APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            if Favorite.objects.filter(user=user).exists():
                favorite_object = Favorite.objects.get(user=user)
                fav_products = favorite_object.products.all()
                recommendations = []
                for product in fav_products:
                    filtered_products = ProductItem.objects.filter(category=product.category)[:6]
                    for filtered_product in filtered_products:
                        recommendations.append(filtered_product)
                product_serializer = ProductItemSerializers(recommendations, many=True)

                return Response(product_serializer.data)
            recs = ProductItem.objects.all()[:10]
            return Response(ProductItemSerializers(recs, many=True).data)
        else:
            return Response(
                "message: user is not authenticated"
            )

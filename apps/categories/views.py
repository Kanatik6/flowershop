from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]

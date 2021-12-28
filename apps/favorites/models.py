from django.db import models

# Create your models here.
from apps.products.models import ProductItem
from apps.users.models import User


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    products = models.ManyToManyField(ProductItem, verbose_name='Продукты')

    class Meta:
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"


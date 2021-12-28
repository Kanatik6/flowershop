from django.contrib.auth import get_user_model
from django.db import models

from apps.carts.models import Cart
from utils.validators import phone_number_validators

User = get_user_model()

PAYMENT_TYPE_CHOICES = (
    ("cart", "cart"),
    ("money", "money"),
)


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="order_cart",
        blank=True,
        null=True,
        verbose_name='Корзина'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_order",
        blank=True,
        null=True,
        verbose_name='Покупатель'
    )
    address = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name='Адрес'
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Фамилия'
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Имя'
    )
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[phone_number_validators],
        blank=True,
        null=True,
        verbose_name='Номер телефона'
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name='Комментарий'
    )
    payment_type = models.CharField(
        choices=PAYMENT_TYPE_CHOICES,
        null=True,
        blank=True,
        max_length=25,
        verbose_name='Способ оплаты'
    )
    total_sum = models.DecimalField(
        decimal_places=2, blank=True, null=True, default=0, max_digits=10,
        verbose_name='Общая сумма заказа'
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.first_name} -- {self.last_name} -- {self.address}"


class ProductOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="product_order_order",
        blank=True,
        null=True,
    )
    title = models.CharField('Название', max_length=255, blank=True, null=True)
    quantity = models.PositiveIntegerField('Количество', blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2, blank=True, null=True, default=0, max_digits=10,
        verbose_name='Цена'
    )

    class Meta:
        verbose_name = "Заказ продукта"
        verbose_name_plural = "Заказ продуктов"

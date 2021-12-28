from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import ProductItem
from apps.carts.managers import CartManager


User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cart',
        verbose_name='Пользователь'
    )
    total_sum = models.IntegerField('Общая цена корзины', blank=True, null=True)

    objects = CartManager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def __str__(self):
        return f"Cart owner is {self.user}"

    @property
    def get_total_quantity_price(self):
        return sum(item.get_total_price() for item in self.cart_items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='cart_items',
        verbose_name='Корзина'
    )
    product = models.ForeignKey(
        ProductItem, on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='product_item_cart',
        verbose_name='Продукт'
    )
    amount = models.PositiveIntegerField(default=1, blank=True, null=True, verbose_name='Количество')

    class Meta:
        verbose_name = "Товар корзины"
        verbose_name_plural = "Товары в корзине"

    def __str__(self):
        if self.cart:
            return f"{self.cart.id} -- {self.product.title}"
        # else:
        #     return f"{self.amount} -- {self.cart_items.total_sum}"

    def get_total_price(self):
        return self.product.price * self.amount
        return f"{self.cart.id} -- {self.product.title} -- {self.amount}"


@receiver(post_save, sender=User)
def create_cart_model(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

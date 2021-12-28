from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    article = models.CharField(max_length=64, blank=True, null=True, verbose_name='Артикул')

    class Meta:
        verbose_name = "Артикул"
        verbose_name_plural = "Артикулы"

    def __str__(self):
        return f"id: {self.id} | article: {self.article}"


"""def get_total_quantity_price(self):
        return sum(product.get_total_price() for product in self.product_items.all())
"""


class ProductItem(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    size = models.CharField(max_length=255, blank=True, null=True, verbose_name='Размер')
    category = models.ForeignKey(
        Category,
        related_name="category",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Категория'
    )
    product = models.ForeignKey(
        Product,
        related_name="product_items",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Продукт'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(
        max_digits=20, decimal_places=2, default=0, blank=True, null=True,
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(blank=True, null=True,verbose_name='Количество')
    equipment = models.TextField(blank=True, null=True, verbose_name='Комплектация')
    is_new = models.BooleanField(blank=True, null=True, default=False, verbose_name='Новый ли продукт?')
    bouquet_care = models.TextField(blank=True, null=True, verbose_name='Уход за букетом')
    specifications = models.TextField(blank=True, null=True, verbose_name='Спецификация')
    discount = models.IntegerField(blank=True, null=True, verbose_name='Скидка')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.title

    def get_total_price(self):
        return self.price * self.quantity


class ProductImage(models.Model):
    image = models.ImageField(upload_to="media/images", null=True, blank=True, verbose_name='Картинка')
    product_id = models.ForeignKey(
        ProductItem,
        related_name="product_image",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Фото продукта"
        verbose_name_plural = "Фото продуктов"

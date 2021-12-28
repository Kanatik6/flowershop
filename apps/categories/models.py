from django.db import models


class Category(models.Model):
    title = models.CharField("Название", max_length=255, blank=True, null=True)
    description = models.TextField("Описание", blank=True, null=True)
    image = models.ImageField(
        "Картинка", upload_to="category_image", blank=True, null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("-id",)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ProductCategories(models.Model):
    """Модель для категории публикаций"""
    title = models.CharField(max_length=155, unique=True)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.title


class Product(models.Model):
    """Модель для публикаций"""
    title = models.CharField(max_length=155)
    description = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=ProductCategories, on_delete=models.CASCADE, related_name='products', default=1)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.title

from django.contrib import admin

from apps.store.models import Product, ProductCategories


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass


@admin.register(ProductCategories)
class AdminProductCategories(admin.ModelAdmin):
    pass

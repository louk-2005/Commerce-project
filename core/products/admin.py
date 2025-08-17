#django files
from django.contrib import admin

#your files
from .models import Product, Category, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ru', 'name_ar', 'parent')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ru', 'name_ar', 'category', 'image')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('parent', 'image')
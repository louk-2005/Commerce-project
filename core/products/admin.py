#django files
from django.contrib import admin

#your files
from .models import Product, Category

admin.site.register(Product)

admin.site.register(Category)
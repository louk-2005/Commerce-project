# django files
from django.urls import path, include

# rest files
from rest_framework.routers import DefaultRouter

# your files
from . import views

app_name = 'products'
router = DefaultRouter()

router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'categories', views.CategoryViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]
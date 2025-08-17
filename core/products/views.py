#rest files
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import action as Action


#your files
from .models import Product, Category, ProductImage
from .serializers import ProductSerializer, CategorySerializer, ProductImageSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_en','name_ru','name_ar', 'description']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "en")  # default 'en'
        context["lang"] = lang
        return context

    @Action(detail=True, methods=['get'])
    def get_product_image(self, request, pk=None):
        product = self.get_object()
        images = ProductImage.objects.filter(parent=product)
        serializer = ProductImageSerializer(
            images, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        lang = self.request.query_params.get("lang", "en")
        context["lang"] = lang
        return context
    @Action(detail=True, methods=['get'])
    def get_products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(
            products, many=True, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_200_OK)






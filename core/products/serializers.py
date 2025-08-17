#rest fiels
from rest_framework import serializers

from .models import Product, Category, ProductImage


#your files


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'category']

    def get_name(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_description(lang)


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'parent', 'products']

    def get_name(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_name(lang)

    def get_description(self, obj):
        lang = self.context.get('lang', 'en')
        return obj.get_description(lang)
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

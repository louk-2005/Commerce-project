#django files
from django.db import models


#package files
from PIL import Image


class Category(models.Model):
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_ar = models.CharField(max_length=100, blank=True, null=True)

    description_en = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='categories/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
    def save(self, *args, **kwargs):
        if self.pk:
            orig = Category.objects.filter(pk=self.pk).first()
            orig_image = orig.image if orig else None
        else:
            orig_image = None

        super().save(*args, **kwargs)

        if self.image and (not orig_image or self.image.name != orig_image.name):
            self.resize_image()
    def get_name(self, lang='en'):
        return getattr(self, f'name_{lang}', self.name_en)

    def get_description(self, lang='en'):
        return getattr(self, f'description_{lang}', self.description_en)

    def __str__(self):
        return self.get_name('en') or "Unnamed Category"

    def resize_image(self):
        image_path = self.image.path
        try:
            with Image.open(image_path) as img:
                target_size = (900, 800)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")

class Product(models.Model):
    name_en = models.CharField(max_length=100,blank=True, null=True)
    name_ru = models.CharField(max_length=100,blank=True, null=True)
    name_ar = models.CharField(max_length=100,blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    description_en = models.TextField(blank=True, null=True)
    description_ru = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='products/')
    def save(self, *args, **kwargs):
        if self.pk:
            orig = Product.objects.filter(pk=self.pk).first()
            orig_image = orig.image if orig else None
        else:
            orig_image = None

        super().save(*args, **kwargs)

        if self.image and (not orig_image or self.image.name != orig_image.name):
            self.resize_image()

    def resize_image(self):
        image_path = self.image.path
        try:
            with Image.open(image_path) as img:
                target_size = (900, 500)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")
    def get_name(self, lang='en'):
        return getattr(self, f'name_{lang}', self.name_en)

    def get_description(self, lang='en'):
        return getattr(self, f'description_{lang}', self.description_en)

    def __str__(self):
        return self.name_en or "Unnamed Product"


class ProductImage(models.Model):
    parent = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/images/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Product.objects.filter(pk=self.pk).first()
            orig_image = orig.image if orig else None
        else:
            orig_image = None

        super().save(*args, **kwargs)

        if self.image and (not orig_image or self.image.name != orig_image.name):
            self.resize_image()

    def resize_image(self):
        image_path = self.image.path
        try:
            with Image.open(image_path) as img:
                target_size = (900, 600)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")

    def __str__(self):
        return f'{self.parent.name_en}'






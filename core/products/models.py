#django files
from django.db import models


#package files
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='categories/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
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
                target_size = (900, 800)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    description = models.TextField()
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

    def __str__(self):
        return self.name










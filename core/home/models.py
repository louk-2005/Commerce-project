from django.db import models

#package files
from PIL import Image

class HomeImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    def save(self, *args, **kwargs):
        if self.pk:
            orig = HomeImage.objects.filter(pk=self.pk).first()
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
                target_size = (1900, 1000)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")
#django files
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#app package
from PIL import Image


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\d{11}$',
        message="Phone number must be exactly 11 digits."
    )
    phone_number = models.CharField(max_length=11, unique=True, validators=[phone_regex], blank=True, null=True)

    def __str__(self):
        return self.username

class ContactInfo(models.Model):
    NAME_CHOICES = [
        ('FACTORY', 'factory'),
        ('CENTRAL_OFFICE', 'Central office'),
        ('SHOW_ROOM', 'Show room'),
    ]
    name = models.CharField(choices=NAME_CHOICES, max_length=55, default='FACTORY')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    description = models.TextField(verbose_name="communicate with us", blank=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.pk:
            orig = ContactInfo.objects.filter(pk=self.pk).first()
            orig_image = orig.logo if orig else None
        else:
            orig_image = None

        super().save(*args, **kwargs)

        if self.logo and self.logo != orig_image:
            image_path = self.logo.path
            with Image.open(image_path) as img:
                max_size = (300, 300)
                img.thumbnail(max_size)
                img.save(image_path, quality=85)

    def __str__(self):
        return "Contact information"


class SocialLink(models.Model):
    contact = models.ForeignKey(ContactInfo, related_name='social_links', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="field name")
    url = models.URLField(verbose_name="link url")
    icon = models.ImageField(upload_to='social_icons/', verbose_name="icon", blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.url}"
class Location(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='location/images', blank=True, null=True)
    description = models.TextField(verbose_name="description", blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")

    def save(self, *args, **kwargs):
        if self.pk:
            orig = Location.objects.filter(pk=self.pk).first()
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
                target_size = (220, 120)
                resized_img = img.resize(target_size, Image.LANCZOS)
                format = img.format or 'JPEG'
                resized_img.save(image_path, format=format, quality=95)
        except Exception as e:
            print(f"Error resizing image: {e}")

class CommunicationWithUs(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\d{11}$',
        message="Phone number must be exactly 11 digits."
    )
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11, unique=True, validators=[phone_regex], blank=True, null=True)
    message = models.TextField(verbose_name="communicate with us", blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email} - {self.phone} - {self.message[:20]}"




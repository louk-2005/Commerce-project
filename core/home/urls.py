#django
from django.urls import path,include

#rest
from rest_framework import routers

#your files
from . import views

app_name = 'home'

router = routers.DefaultRouter()
router.register(r'images', views.HomeImageViewSet, basename='home_images')
urlpatterns = [
    path('', include(router.urls)),
]
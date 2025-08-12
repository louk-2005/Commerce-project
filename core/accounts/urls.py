#django files
from django.urls import path,include

#rest files
from rest_framework.routers import DefaultRouter
#your files
from . import views

app_name = 'accounts'
router = DefaultRouter()

router.register(r'contact', views.ContactViewSet, basename='contact')
router.register(r'social/links', views.SocialLinkViewSet, basename='social')

urlpatterns = [
    path('', include(router.urls)),
]

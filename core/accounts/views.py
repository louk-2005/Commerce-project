from django.shortcuts import render

#rest files
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


#your files
from .models import ContactInfo,SocialLink
from .serializers import ContactInfoSerializer,SocialLinkSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer










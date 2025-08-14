from django.shortcuts import render

#rest files
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import action as Action


#your files
from .models import ContactInfo,SocialLink, Location,CommunicationWithUs
from .serializers import ContactInfoSerializer,SocialLinkSerializer, LocationSerializer, CommunicationWithUsSerializer



class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

    @Action(detail=True, methods=['get'])
    def get_social_links(self, request, pk=None):
        contact = self.get_object()
        social_links = SocialLink.objects.filter(contact=contact)
        serializer = SocialLinkSerializer(social_links, many=True)
        return Response(serializer.data)

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class CommunicationWithUsViewSet(viewsets.ModelViewSet):
    queryset = CommunicationWithUs.objects.all()
    serializer_class = CommunicationWithUsSerializer





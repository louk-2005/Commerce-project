#rest framework
from rest_framework import serializers

#your files
from .models import ContactInfo, SocialLink, Location, CommunicationWithUs



class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = '__all__'
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class CommunicationWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationWithUs
        fields = '__all__'





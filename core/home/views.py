#rest files
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


#your files
from .models import HomeImage
from .serializers import HomeImageSerializer


class HomeImageViewSet(viewsets.ModelViewSet):
    queryset = HomeImage.objects.all()
    serializer_class = HomeImageSerializer

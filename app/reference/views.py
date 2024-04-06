from django.shortcuts import render
from rest_framework import status,generics, viewsets
from .models import Part
from .serializers import PartSerializer
# Create your views here.


class PartAPIList(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
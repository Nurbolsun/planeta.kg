from django.shortcuts import render
from rest_framework import status, generics, viewsets
from .models import *
from .serializers import *
# Create your views here.


class PartAPIList(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer


class CategoryAPIList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RefCarMarkAPIList(viewsets.ModelViewSet):
    queryset = RefCarMark.objects.all()
    serializer_class = RefCarMarkSerializer


class RefCarModelAPIList(viewsets.ModelViewSet):
    queryset = RefCarModel.objects.all()
    serializer_class = RefCarModelSerializer


class RefCarGearBoxAPIList(viewsets.ModelViewSet):
    queryset = RefCarGearBox.objects.all()
    serializer_class = RefCarGearBoxSerializer


class RefCarBodyAPIList(viewsets.ModelViewSet):
    queryset = RefCarBody.objects.all()
    serializer_class = RefCarBodySerializer
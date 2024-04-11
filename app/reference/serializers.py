from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PartImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartImage
        fields = '__all__'


class RefCarMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarMark
        fields = ('name_ru', 'emblems')


class RefCarFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarFuel
        fields = 'name_ru'


class RefCarGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarGearBox
        fields = 'name_ru'


class RefCarSteeringWheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarSteeringWheel
        fields = 'name_ru'


class RefCarWheelDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarWheelDrive
        fields = 'name_ru'


class RefCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarModel
        fields = '__all__'


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'


class RefCarBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefCarBody
        fields = '__all__'
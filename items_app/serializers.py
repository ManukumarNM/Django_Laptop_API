from rest_framework import serializers
from .models import LaptopsModel


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopsModel
        fields = ['id', 'name', 'brand','price']

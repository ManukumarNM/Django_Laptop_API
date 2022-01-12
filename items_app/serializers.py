from django.contrib.auth.models import User
from rest_framework import serializers
from .models import LaptopsModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class LaptopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LaptopsModel
        fields = ['id', 'name', 'brand','price']

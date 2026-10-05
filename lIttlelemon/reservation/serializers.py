from django.contrib.auth.models import User
from .models import BookingTable, MenuList
from rest_framework import serializers

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class MenuListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuList
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
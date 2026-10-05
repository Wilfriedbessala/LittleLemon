from django.contrib.auth.models import User
from .models import BookingTable, MenuTable
from rest_framework import serializers

class BookingTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'

class MenuTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuTable
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
# Create your views here.
from rest_framework.decorators import api_view
from .models import BookingTable, MenuList
from .serializers import MenuListSerializer, BookingTableSerializer, UserSerializer

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuList.objects.all()
    serializer_class = MenuListSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookingTable.objects.all()
    serializer_class = BookingTableSerializer
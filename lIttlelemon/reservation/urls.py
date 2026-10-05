from django.urls import path
from .views import MenuItemsView, SingleMenuItemView

urlpatterns =[
    path('menu/', MenuItemsView.as_view()),
    path('table/<int:pk>', SingleMenuItemView.as_view()),
]
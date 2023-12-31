from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('fullremove/<int:product_id>/',views.full_remove,name='full_remove'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove')
]

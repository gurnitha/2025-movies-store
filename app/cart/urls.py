# app/cart/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'cart'

urlpatterns = [
      path('cart/', views.cart_list_view, name='cart_list'),
      path('cart/<int:id>/add/', views.cart_add_view, name='cart_add'),
      path('cart/clear/', views.cart_clear_view, name='cart_clear'),
      path('cart/purchase/', views.cart_purchase_view, name='cart_purchase'),
]


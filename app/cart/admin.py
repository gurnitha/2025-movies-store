# app/cart/admin.py
from django.contrib import admin

# Local
from .models import Order

# Register your models here.

admin.site.register(Order)

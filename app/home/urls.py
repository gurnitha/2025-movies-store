# app/home/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
]


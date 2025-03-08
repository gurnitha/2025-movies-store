# app/accounts/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'accounts'

urlpatterns = [
    path('accounts/signup', views.signup_view, name='signup'),
]

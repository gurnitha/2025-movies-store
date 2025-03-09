# app/accounts/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'accounts'

urlpatterns = [
    path('accounts/signup', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', views.orders_view, name='orders'),
]

















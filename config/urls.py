# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # home
    path('', include('home.urls', namespace='home')),
    # movies
    path('', include('movies.urls', namespace='movies')),
    # admin
    path('admin/', admin.site.urls),
]

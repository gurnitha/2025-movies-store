# app/movies/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'movies'

urlpatterns = [
    path('movies/', views.movies_view, name='movies'),
]


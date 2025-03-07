# app/movies/admin.py
from django.contrib import admin

# Local
from .models import Movie

# Register your models here.

admin.site.register(Movie)
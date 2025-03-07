# app/movies/admin.py
from django.contrib import admin

# Local
from .models import Movie

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	ordering = ['name']

admin.site.register(Movie, MovieAdmin)
























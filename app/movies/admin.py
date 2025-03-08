# app/movies/admin.py
from django.contrib import admin

# Local
from .models import Movie, Review

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
	ordering = ['name']
	search_fields = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
























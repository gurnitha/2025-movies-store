# app/movies/views.py
from django.shortcuts import render

# Create your views here.

def movies_view(request):
	context = {
		'page_title': 'Movies',
	}
	return render(request, 'movies/movies.html', context)


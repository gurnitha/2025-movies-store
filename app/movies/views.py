# app/movies/views.py
from django.shortcuts import render

# Local
from .models import Movie

# Create your views here.

def movies_view(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    context = {
        'template_data': template_data,
    }
    return render(request, 'movies/movies.html', context)


def movie_view(request, id):
    movie = movies[id - 1]
    template_data = {}
    template_data['title'] = movie['name']
    template_data['movie'] = movie
    context = {
        'page_title': template_data['title'],
        'template_data': template_data,
    }
    return render(request, 'movies/movie.html', context)






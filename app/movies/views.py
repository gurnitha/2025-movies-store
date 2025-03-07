# app/movies/views.py
from django.shortcuts import render

# Local
from .models import Movie

# Create your views here.

def movies_view(request):
    # Seearch
    search_term = request.GET.get('search')
    if search_term:
        movies = Movie.objects.filter(name__icontains=search_term)
    else:
        movies = Movie.objects.all()
    # Search ends

    template_data = {}
    template_data['title'] = 'Movies'
    # template_data['movies'] = Movie.objects.all()
    template_data['movies'] = movies
    context = {
        'template_data': template_data,
    }
    return render(request, 'movies/movies.html', context)


def movie_view(request, id):
    movie =  Movie.objects.get(id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    context = {
        'template_data': template_data,
    }
    return render(request, 'movies/movie.html', context)






# app/movies/views.py
from django.shortcuts import render

# Create your views here.


movies = [
    {
        'id': 1, 'name': 'Inception', 'price': 12,
        'description': 'A mind-bending heist thriller.'
    },
    {
        'id': 2, 'name': 'Avatar', 'price': 13,
        'description': 'A journey to a distant world and the battle for resources.'
    },
    {
        'id': 3, 'name': 'The Dark Knight', 'price': 14,
        'description': 'Gothams vigilante faces the Joker.'
    },
    {
        'id': 4, 'name': 'Titanic', 'price': 11,
        'description': 'A love story set against the backdrop of the sinking Titanic.',
    },
]

def movies_view(request):
    template_data = {}
    template_data['movies'] = movies
    context = {
        'page_title': 'Movies',
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






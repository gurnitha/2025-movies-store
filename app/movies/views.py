# app/movies/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Local
from .models import Movie, Review

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


@login_required
def create_review_view(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        movie = Movie.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.movie = movie
        review.user = request.user
        review.save()
        return redirect('movies:movie', id=id)
    else:
        return redirect('movies:movie', id=id)




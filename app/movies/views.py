# app/movies/views.py
from django.shortcuts import render, redirect, get_object_or_404
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
    reviews = Review.objects.filter(movie=movie)

    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    template_data['reviews'] = reviews
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


@login_required
def edit_review_view(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('movies.show', id=id)

    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'movies/edit_review.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('movies:movie', id=id)
    else:
        return redirect('movies:movie', id=id)
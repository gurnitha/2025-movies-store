# app/movies/urls.py
from django.urls import path

# Local
from . import views

# namespace
app_name = 'movies'

urlpatterns = [
    path('movies/', views.movies_view, name='movies'),
    path('movie/<int:id>/', views.movie_view, name='movie'),
    path('movie/<int:id>/review/create/', views.create_review_view, name='create_review'),
    path('movie/<int:id>/review/<int:review_id>/edit/', views.edit_review_view, name='edit_review'),
    path('movie/<int:id>/review/<int:review_id>/delete/', views.delete_review_view, name='delete_review'),
]


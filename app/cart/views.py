# app/cart/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

# Local
from movies.models import Movie
from .utils import calculate_cart_total

# Create your views here.

def cart_add_view(request, id):
    get_object_or_404(Movie, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart:cart_list')


def cart_list_view(request):
    cart_total = 0
    movies_in_cart = []
    cart = request.session.get('cart', {})
    movie_ids = list(cart.keys())
    if (movie_ids != []):
        movies_in_cart = Movie.objects.filter(id__in=movie_ids)
        cart_total = calculate_cart_total(cart, movies_in_cart)

    template_data = {}
    template_data['title'] = 'Cart'
    template_data['movies_in_cart'] = movies_in_cart
    template_data['cart_total'] = cart_total
    context = {
        'template_data': template_data,
    }
    return render(request, 'cart/cart_list.html', context)


def cart_clear_view(request):
    request.session['cart'] = {}
    return redirect('cart:cart_list')
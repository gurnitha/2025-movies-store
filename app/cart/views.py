# app/cart/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Local
from movies.models import Movie
from .utils import calculate_cart_total
from .models import Order, Item

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


# Dekorator login_required untuk memastikan bahwa pengguna
# harus masuk untuk mengakses fungsi pembelian.
@login_required
# Fungsi pembelian, yang akan menangani proses pembelian.
def cart_purchase_view(request):
    # Ambil data keranjang dari sesi pengguna.
    # Variabel keranjang akan berisi kamus dengan
    # ID movie sebagai kunci dan kuantitas sebagai nilai.
    cart = request.session.get('cart', {})
    # Ambil ID movie yang disimpan di dict keranjang
    # dan mengubahnya menjadi daftar bernama movie_ids.
    movie_ids = list(cart.keys())

    # Periksa apakah daftar movie_ids kosong (yang
    # menunjukkan keranjang kosong). Dalam hal ini,
    # pengguna diarahkan ke halaman cart.index (di sini,
    # fungsi pembelian menyelesaikan eksekusinya).
    if (movie_ids == []):
        return redirect('cart:cart_list')
    
    # Jika keranjang tidak kosong, kami melanjutkan proses pembelian.

    # Ambil objek movie dari database berdasarkan
    # ID yang disimpan di keranjang menggunakan Movie
    movies_in_cart = Movie.objects.filter(id__in=movie_ids)
    # Hitung total biaya movie di keranjang
    # menggunakan fungsi calculate_cart_total()
    cart_total = calculate_cart_total(cart, movies_in_cart)

    # Buat objek Order baru. Kami mengatur atributnya
    # seperti user (pengguna yang masuk) dan
    # total (total keranjang), dan simpan ke database.
    order = Order()
    order.user = request.user
    order.total = cart_total
    order.save()

    # Iterasi movie di keranjang. Kami membuat Item
    # untuk setiap movie di keranjang. Untuk setiap Item, kami mengatur
    # harga dan kuantitasnya, tautkan movie yang sesuai dan
    # pesan, dan simpan ke database.
    for movie in movies_in_cart:
        item = Item()
        item.movie = movie
        item.price = movie.price
        item.order = order
        item.quantity = cart[str(movie.id)]
        item.save()

    # Setelah pembelian selesai, kami menghapus keranjang di
    # sesi pengguna dengan mengatur request.session['cart']
    # ke kamus kosong.
    request.session['cart'] = {}
    # Kunjungi data yang akan dikirim ke konfirmasi pembelian
    # templat. Data ini mencakup judul halaman
    # dan ID pesanan yang dibuat.
    template_data = {}
    template_data['title'] = 'Purchase confirmation'
    template_data['order_id'] = order.id
    context = {
        'template_data': template_data,
    }
    # Terakhir, render template cart/purchase.html.
    return render(request, 'cart/purchase.html', context)
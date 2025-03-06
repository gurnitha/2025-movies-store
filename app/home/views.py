# app/home/views.py
from django.shortcuts import render

# Create your views here.

def home_view(request):
	context = {
		'page_title': 'Home',
	}
	return render(request, 'home/home.html', context)


def about_view(request):
	context = {
		'page_title': 'About',
	}
	return render(request, 'home/about.html', context)


def contact_view(request):
	context = {
		'page_title': 'Contact',
	}
	return render(request, 'home/contact.html', context)

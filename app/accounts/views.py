# app/accounts/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup_view(request):

	template_data = {}
	template_data['title'] = 'Sign Up'

	# Handling GET method request
	if request.method == 'GET':
		template_data['form'] = UserCreationForm()

	context = {
		'template_data': template_data,
	}

	return render(request, 'accounts/signup.html', context)


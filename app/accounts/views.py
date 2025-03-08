# app/accounts/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import CustomUserCreationForm

# Create your views here.

def signup_view(request):

	template_data = {}
	template_data['title'] = 'Sign Up'

	# Handling GET method request
	if request.method == 'GET':
		template_data['form'] = CustomUserCreationForm()
		context = {
			'template_data': template_data,
		}
		return render(request, 'accounts/signup.html', context)

	# Handling POST method request
	elif request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home:home')
		else:
			template_data['form'] = form
			context = {
				'template_data': template_data,
			}
			return render(request, 'accounts/signup.html', context)

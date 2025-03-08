# app/accounts/views.py
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login, authenticate
from .forms import CustomUserCreationForm, CustomErrorList

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
        form = CustomUserCreationForm(request.POST, 
            error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            template_data['form'] = form
            context = {
                'template_data': template_data,
            }
            return render(request, 'accounts/signup.html', context)


def login_view(request):

    template_data = {}
    template_data['title'] = 'Login'

    # Handling GET method request
    if request.method == 'GET':
        context = {
            'template_data': template_data,
        }
        return render(request, 'accounts/login.html', context)

    # Handling POST method request
    elif request.method == 'POST':
        user = authenticate(
            request, 
            username = request.POST['username'], 
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            context = {
                'template_data': template_data,
            }
            return render(request, 'accounts/login.html', context)
        else:
            auth_login(request, user)
            return redirect('home:home')
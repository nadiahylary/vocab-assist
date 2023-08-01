from django.contrib import auth, messages
from django.contrib.auth import views, authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import CustomUser


# Create your views here.


def login_user(request):
    if request.method == 'POST':
        # email = request.POST['email']
        # password = request.POST['password']
        email = request.user.email
        password = request.user.password
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Successfully Logged in!")
            return redirect('dictionary:index', user)
        else:
            messages.error(request, "There was an error. Please try again...or signup!")
            return redirect('dictionary:index')
    else:
        return render(request, 'custom_auth/login.html', {'form': AuthenticationForm})


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Auto authenticate the user:
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Your account was Successfully Created! Cheers!")
            return redirect('dictionary:index')
    else:
        form = RegisterForm()
        return render(request, 'custom_auth/signup.html', {'form': form})
    return render(request, 'custom_auth/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been Successfully Logged Out! See you next time ;)")
    return redirect('/login')


def index(request):
    user = request.user
    return render(request, 'custom_auth/index.html', {'user': user})

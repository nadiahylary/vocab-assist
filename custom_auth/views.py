from django.contrib import auth
from django.contrib.auth import views
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import CustomUser


# Create your views here.


class LoginView(views.LoginView):
    form_class = AuthenticationForm
    template_name = 'custom_auth/login.html'
    success_url = reverse_lazy('custom_auth:index')


class SignupView(CreateView):
    form_class = RegisterForm
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy('custom_auth:login')


def index(request):
    return render(request, 'custom_auth/index.html')



from django.contrib import auth
from django.contrib.auth import views
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm


# Create your views here.


class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'custom_auth/login.html'
    success_url = reverse_lazy('dictionary:index')


class SignupView(CreateView):
    form_class = RegisterForm
    template_name = 'custom_auth/signup.html'
    success_url = reverse_lazy('custom_auth:login')

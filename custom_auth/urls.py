from django.contrib import admin
from django.urls import path, include

from custom_auth import views

app_name = 'custom_auth'
urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup')
]

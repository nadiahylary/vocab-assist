from django.contrib import admin
from django.urls import path, include

from custom_auth import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='index'),
]

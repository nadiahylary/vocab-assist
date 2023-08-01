from django.contrib import admin
from django.urls import path, include

from custom_auth import views

app_name = 'custom_auth'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout_user, name='logout')
]

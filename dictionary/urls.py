from django.contrib import admin
from django.urls import path, include

from dictionary import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:word>', views.DetailView.as_view(), name='define'),
    path('<str:word>/antonyms', views.AntonymsView.as_view(), name='antonyms'),
    path('<str:word>/synonyms', views.SynonymsView.as_view(), name='synonyms'),
    path('<str:word>/usage', views.ExamplesView.as_view(), name='usage'),
]
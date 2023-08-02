from django.urls import path
from dictionary import views

app_name = 'dictionary'
urlpatterns = [
    # the home page, shows a random word, recent saved words, search bar and random quote
    path('', views.IndexView.as_view(), name='index'),
    # the view that handles a submit action in the search bar of the index/home page
    path('<str:text>/', views.SearchView.as_view(), name='search'),
    # on select/click of a word amongst the search results, this view handles that action. Shows the details of the word
    path('<str:word>/', views.DetailView.as_view(), name='define'),
    # this view handles a click on antonyms of a given word
    path('<str:word>/antonyms', views.AntonymsView.as_view(), name='antonyms'),
    # this view handles a click on synonyms of a given word
    path('<str:word>/synonyms', views.SynonymsView.as_view(), name='synonyms'),
    # this view handles a click on examples of usage of a given word
    path('<str:word>/usage', views.ExamplesView.as_view(), name='usage')
]

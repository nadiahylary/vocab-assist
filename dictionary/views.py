from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from random_word import RandomWords
from PyDictionary import PyDictionary

r_word = RandomWords().get_random_word()
my_dict = PyDictionary()

# Create your views here.


class IndexView(View):

    def get(self, request):
        word = "prolific"
        meanings = my_dict.meaning(word)
        synonyms = my_dict.getSynonyms(word)
        antonyms = my_dict.getAntonyms(word)

        context = {
            'word': word,
            'meanings': meanings,
            'synonyms': synonyms,
            'antonyms': antonyms
        }
        return render(request, "dictionary/index.html", context)


class SearchView(View):
    pass


class DetailWordView(DetailView):
    pass


class AntonymsView(ListView):
    pass


class SynonymsView(ListView):
    pass


class ExamplesView(ListView):
    pass

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from dictionary.models import Word


# Create your views here.

# @login_required(login_url='custom_auth:login')
class IndexView(View):

    def get(self, request):
        words = Word.objects.all()
        context = {
            "words": words,
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

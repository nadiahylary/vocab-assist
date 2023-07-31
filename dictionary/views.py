from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

app_name = 'dictionary'
# Create your views here.


class IndexView(View):
    pass


class DetailWordView(DetailView):
    pass


class AntonymsView(ListView):
    pass


class SynonymsView(ListView):
    pass


class ExamplesView(ListView):
    pass

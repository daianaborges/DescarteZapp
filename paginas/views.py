# from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = "index.html"

class HomeView(TemplateView):
    template_name = "home.html"

from django.shortcuts import render
from django.views.generic import TemplateView

class homeView(TemplateView):
    template_name = "index.html"
from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class UploadView(TemplateView):
    template_name = "upload.html"
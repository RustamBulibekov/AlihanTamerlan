from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FirstView(TemplateView):
    template_name = 'first.html'
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog

# Create your views here.
class HomePageView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'home.html'
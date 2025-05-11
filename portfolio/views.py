from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog

# Create your views here.
# class HomePageView(ListView):
#     model = Blog
#     context_object_name = 'blogs'
#     template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'portfolio/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'about'
        return context 


class BlogView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'portfolio/blog.html'

class TutorialView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='tutorial')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'tutorial'
        return context 

class ProjectView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='app')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'app'
        return context 

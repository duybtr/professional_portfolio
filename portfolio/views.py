from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Blog

# Create your views here.
# class HomePageView(ListView):
#     model = Blog
#     context_object_name = 'blogs'
#     template_name = 'home.html'

class BlogView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'portfolio/blog.html'

class ArticleView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='article')

class ProjectView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='app')

class VideoView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='video')
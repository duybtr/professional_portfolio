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

class ArticleView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='article')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'article'
        return context 

class ProjectView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='app')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'app'
        return context 

class VideoView(BlogView):
    def get_queryset(self):
        return Blog.objects.filter(category='video')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = 'video'
        return context 

def get_screenshot(request, blog_pk):
    blog = Blog.objects.get(pk=blog_pk)
    context = {}
    context['blog'] = blog
    return render(request, 'portfolio/partial/screenshot_modal.html', context) 
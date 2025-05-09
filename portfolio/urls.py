from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, ArticleView, ProjectView, VideoView, get_screenshot

urlpatterns = [
    path('', ProjectView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('get_videos', VideoView.as_view(), name='get_videos'),
    path('get_articles', ArticleView.as_view(), name='get_articles'),
    path('get_projects', ProjectView.as_view(), name='get_projects'),
    path('<int:blog_pk>/get_screenshot', get_screenshot, name='get_screenshot')
]
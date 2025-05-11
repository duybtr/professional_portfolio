from django.urls import path
from django.views.generic import TemplateView
from .views import AboutView, TutorialView, ProjectView

urlpatterns = [
    path('', ProjectView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('get_tutorials', TutorialView.as_view(), name='get_tutorials'),
    path('get_projects', ProjectView.as_view(), name='get_projects')
]
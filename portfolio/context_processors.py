from .models import Blog
from django.db.models import Q

def count_blogs(request):
    project_count = Blog.objects.filter(category='app').count()
    tutorial_count = Blog.objects.filter(category='tutorial').count()
    return {
        'project_count' : project_count,
        'tutorial_count' : tutorial_count
    }

from .models import Blog
from django.db.models import Q

def count_blogs(request):
    project_count = Blog.objects.filter(category='app').count()
    article_count = Blog.objects.filter(category='article').count()
    video_count = Blog.objects.filter(category='video').count()
    return {
        'project_count' : project_count,
        'article_count' : article_count,
        'video_count' : video_count
    }

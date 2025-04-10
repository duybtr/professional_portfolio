from django.db import models

# Create your models here.
class Blog(models.Model):
    choices = [
        ('app', 'app'),
        ('article', 'article'),
        ('video', 'video')
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=choices, default='app')
    link = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    repo_link = models.CharField(max_length=200, blank=True)
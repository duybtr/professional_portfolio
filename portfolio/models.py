from django.db import models

# Create your models here.
class Blog(models.Model):
    choices = [
        ('app', 'app'),
        ('tutorial', 'tutorial'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=choices, default='app')
    site_link = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    repo_link = models.CharField(max_length=200, blank=True)
    screenshot_url = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
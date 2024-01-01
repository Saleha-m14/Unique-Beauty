from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=False)
    featured_image = models.ImageField('blog_image', default='placeholder')
    alt_tag = models.CharField(max_length=50, default='Blog image')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.title
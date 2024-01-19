from django.db import models
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=False)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    featured_image = models.ImageField('blog_image', default='placeholder')
    alt_tag = models.CharField(max_length=50, default='Blog image')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.title
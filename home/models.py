from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone
# Create your models here.
# contact form

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name


# Newsletter Subscribers

class NewsletterSubscribers(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, max_length=100)
    subscribed_on = models.DateTimeField('Subscribed on', default=timezone.now)

    def __str__(self):
        return self.email
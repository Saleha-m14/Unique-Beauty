from django.db import models
from django.core.validators import EmailValidator
# Create your models here.
# contact form

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name
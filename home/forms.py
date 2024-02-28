from django import forms
from .models import Contact
from tinymce.widgets import TinyMCE

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    recievers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
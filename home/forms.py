from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    recievers = forms.CharField()
    message = forms.CharField(label="Email content")
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject= request.POST['subject']
        email = request.POST['email']
        send_mail(
            'Contact Form',  #title
            'message',  #message
            'settings.EMAIL_HOST_USER', #sender if not available consider
            [email],  # reciever email
            fail_silently=False
        )
        print(send_mail)
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save(commit=False)
            messages.success(request, 'Thanks for contacting us!')
        else:
            messages.error(request, 'Please fill the contact form to get in touch.')
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)

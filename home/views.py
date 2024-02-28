from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscribers
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.

def index(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        name = request.POST.get('name', '')
        subject = request.POST.get('subject', '')
        email = request.POST.get('email', '')
        send_mail(
            'Unique Beauty Contact Form',  #title
            f'Hello {name}, thanks for contacting us!\nWe rescieved your message that is:\n\n{message}\n\nPlease note that your message will be reviewed.\n\nCheck out the new perfum and hair products that are added to the store.\nLink - https://unique-beauty-p5-092d291f63b2.herokuapp.com/products/\n\n',  #message
            'settings.EMAIL_HOST_USER', #sender if not available consider
            [email],  # reciever email
            fail_silently=False
        )
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

def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if not name or not email:
            messages.error(request, 'In order to subscribe for newsletter name and email is required!')
            return redirect("/")

        newsletter_subscriber = NewsletterSubscribers.objects.filter(email=email).first()
        if newsletter_subscriber:
            messages.error(request, f'{email}this email address is already a newsletter subscriber!')
            return redirect(request.META.get("HTTP_REFERER", "/"))
        
        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = NewsletterSubscribers()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(request, f'{email} email was subscribed to our newsletter!')
        return redirect(request.META.get("HTTP_REFERER", "/"))


def newsletter(request):
    return redirect('/')
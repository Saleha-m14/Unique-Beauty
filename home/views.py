from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import NewsletterSubscribers
# Create your views here.

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        name = request.POST['name']
        subject= request.POST['subject']
        email = request.POST['email']
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
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(request, "In order to subscribe for newsletter name and email is required!")
            return redirect("/")
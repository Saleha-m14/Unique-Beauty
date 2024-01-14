from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
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

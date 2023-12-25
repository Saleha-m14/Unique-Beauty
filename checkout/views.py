from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from shopping_bag.contexts import shopping_bag.contents

import stripe
# checkout view
def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "Your bag is empty at the moment.")
        return redirect(reverse('products'))

    current_bag = shopping_bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ORAZ3D4bddW0mwgJumHxeLLNEL8cBCkQKt8P6oKwlbKM78TC9klca4hVXXsPbSDgWc0TVBFRKC3B458SjXow3Yt00ILmy4Dbl',
        'client_secret': 'test client secret',
    }
    
    return render(request, template,)

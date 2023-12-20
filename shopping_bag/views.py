from django.shortcuts import render, redirect, reverse

# Create your views here.

def shopping_bag(request):
    """
    This view will return the items that are in the shopping bag.
    """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """
    The view to add a quantity of the specified product to the shopping bag.
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:    
        shopping_bag[item_id] = quantity
    
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    
    """
    This view will ajdust the qunatity of the specified product
    to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
    else:    
        shopping_bag.pop[item_id]
    
    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('shopping_bag'))



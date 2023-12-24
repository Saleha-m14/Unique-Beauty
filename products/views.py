from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product
# Create your views here.

def all_products(request):
    """
    This is a view to return all the products
    """
    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        
    context = {
        'products': products, 
        'search_term': query,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
    This view will return all the details of a product on a seprate page(product_detail.html)
    """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)



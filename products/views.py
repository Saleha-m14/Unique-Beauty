from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):
    """
    This is a view to return all the products
    """
    products = Product.objects.all()
    context = {
        'products': products
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



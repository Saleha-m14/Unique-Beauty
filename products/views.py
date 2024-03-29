from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def all_products(request):
    """
    This is a view to return all the products
    """
    products = Product.objects.all()
    query = None
    categories = None
    direction = None
    sort = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey == 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
        
    context = {
        'products': products, 
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
    This view will return all the details of a product on a seprate page(product_detail.html)
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    reviewform = ReviewForm(request.POST)
    if request.method == 'POST':
        if reviewform.is_valid():
            reviewform.instance.email = request.user.email
            reviewform.instance.name = request.user.username
            review = reviewform.save(commit=False)
            review.product = product
            reviewform.save()
            messages.info(request, "Your review is added!")
        else:
            review_form = ReviewForm()
            return redirect(reverse('product_detail', args=[product_id]))
    context = {
        'product': product,
        'review': reviews,
        'reviewed': False,
        'review_form': ReviewForm()
    }
    return render(request, 'products/product_detail.html', context)

# view for adding a product
@login_required
def add_product(request):
    """
    This div will be used to add product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do it.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'The product is added successfully!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Faild to add a product. Please check the form to ensure it is valid.')
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    
    context = {
        'form': form,
    }

    return render(request, template, context)

# the view to edit a product
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do it.')
        return redirect(reverse('home'))


    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# deleting functionality for superuser
@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only the store owner can do it.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product is deleted!')
    return redirect(reverse('products'))

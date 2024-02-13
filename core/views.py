from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from product.models import Product
from .models import Wishlist
# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')


def add_to_wishlist(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
        if request.user.is_authenticated:
            # Authenticated user
            Wishlist.objects.get_or_create(user=request.user, product=product)
            messages.success(request, 'Product Added to Wishlist')
        else:
            # Unauthenticated user
            wishlist = request.session.get('wishlist', [])
            messages.success(request, 'Product Added to Wishlist')
            if product_id not in wishlist:
                wishlist.append(product_id)
                request.session['wishlist'] = wishlist
    except Exception as e:
        messages.error(request, 'Internal Server Error')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_from_wishlist(request, product_id):
    try:
        if request.user.is_authenticated:
            # Authenticated user
            wishlist= get_object_or_404(Wishlist, product__id=product_id, user=request.user)
            wishlist.delete()
            messages.success(request, 'Product Removed from Wishlist')
        else:
            # Unauthenticated user
    
            wishlist = request.session.get('wishlist', [])
            if product_id in wishlist:
                wishlist.remove(product_id)
                request.session['wishlist'] = wishlist
                messages.success(request, 'Product Removed from Wishlist')
    except Exception as e:
        messages.error(request, f'Internal Server Error{e}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def wishlist(request):
    wishlist_items = None
    if request.user.is_authenticated:
        wishlist_items = Wishlist.objects.filter(user=request.user)
    else:
        wishlist_ids = request.session.get('wishlist', [])
        wishlist_items = Product.objects.filter(id__in=wishlist_ids)
        
    context = {
        'wishlist_items':wishlist_items,
    }
    return render(request, 'wishlist/wishlist.html', context)


def checkout(request):
    return render(request, 'checkout/checkout.html')


def cart(request):
    return render(request, 'cart/cart.html')

def faq(request):
    return render(request, 'faq/faq.html')


def custom_404_view(request, exception):
    return render(request, '404/404.html', status=404)
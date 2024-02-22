from django.shortcuts import render, get_object_or_404
from babel.numbers import format_currency
from django.http import HttpResponseRedirect

from django.conf import settings
from user.models import ShippingAddress

# Create your views here.
def checkout(request):
    shipping_price = 0
    user_shipping_address = None
    items_and_shipping_price = None
    stripe_public_key= settings.STRIPE_PUBLIC_KEY
    client_secret= settings.CLIENT_SECRET_KEY
    
    if request.user.is_authenticated:
        user_shipping_address=  get_object_or_404(ShippingAddress, user=request.user)
    
    if request.method == 'POST':
        items_and_shipping_price= request.POST['items_and_shipping_price']
        formatted_grand_total= format_currency(items_and_shipping_price, 'EUR', locale='en_US')
        selected_shipping_method= request.POST['selected_shipping_method']
        
        if selected_shipping_method == "Express Shipping":
            shipping_price = settings.SHIPPING_METHOD_EXPRESS
        elif selected_shipping_method == "Standard Shipping":
            shipping_price = settings.SHIPPING_METHOD_STANDARD
        else:
            shipping_price = 0
        
    context ={
        "items_and_shipping_price":items_and_shipping_price,
        "formatted_grand_total":formatted_grand_total,
        "shipping_price":shipping_price,
        "shipping_address":user_shipping_address,
        "formatted_shipping_price":format_currency(shipping_price, 'EUR', locale='en_US'),
        "selected_shipping_method":selected_shipping_method,
        "stripe_public_key":stripe_public_key,
        "client_secret":client_secret,
    }
    return render(request, 'checkout/checkout.html', context)


def place_order(request):
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
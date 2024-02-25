from django.shortcuts import render, get_object_or_404, redirect, reverse
from babel.numbers import format_currency
from django.http import HttpResponseRedirect
import stripe
from django.contrib import messages
from django.core.mail import EmailMessage

from django.conf import settings
from user.models import ShippingAddress
from cart import context_processors
from .forms import OrderForm
from .models import Order, OrderLineItem
from cart.models import Cart
from product.models import Product

# Create your views here.
def checkout(request):
    shipping_price = 0
    user_shipping_address = None
    items_and_shipping_price = None
    stripe_public_key= settings.STRIPE_PUBLIC_KEY
    client_secret= settings.CLIENT_SECRET_KEY
    context= context_processors.cart_item(request)
    full_cart_item=context['full_cart_item']
    
    if request.user.is_authenticated:
        user_shipping_address=  get_object_or_404(ShippingAddress, user=request.user)
    
    if request.method == 'POST':
        form_data ={
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone': request.POST['phone'],
            'street_address': request.POST['street_address'],
            'post_code': request.POST['post_code'],
            'city': request.POST['city'],
            'state': request.POST['state'],
            'country': request.POST['country'],
            'shipping_method': request.POST['shipping_method'],
            'shipping_price': request.POST['shipping_price'],
            'sub_total': request.POST['sub_total'],
            'grand_total': request.POST['grand_total'],
        }
        
        order_form = OrderForm(form_data)
        
        if order_form.is_valid():
            order = order_form.save()
            
            if request.user.is_authenticated:
                request_user_id=  request.user.id
                order.user_id =request_user_id
                order.save()
                
            for item in full_cart_item:
                order_line_item = OrderLineItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity
                )
                
                order_line_item.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            return messages.error(request,'Your form is invalid')
        
    else:
        items_and_shipping_price= request.GET['items_and_shipping_price']
        formatted_grand_total= format_currency(items_and_shipping_price, 'EUR', locale='en_US')
        selected_shipping_method= request.GET['selected_shipping_method']
        
        if selected_shipping_method == "Express Shipping":
            shipping_price = settings.SHIPPING_METHOD_EXPRESS
        elif selected_shipping_method == "Standard Shipping":
            shipping_price = settings.SHIPPING_METHOD_STANDARD
        else:
            shipping_price = 0
            
            
        grand_total= float(items_and_shipping_price)
        stripe_total = round(grand_total * 100)
        
        stripe.api_key = client_secret
        intent=stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
              

    context ={
        "items_and_shipping_price":items_and_shipping_price,
        "formatted_grand_total":formatted_grand_total,
        "shipping_price":shipping_price,
        "formatted_shipping_price":format_currency(shipping_price, 'EUR', locale='en_US'),
        "selected_shipping_method":selected_shipping_method,
        "shipping_address":user_shipping_address,
        "stripe_public_key":stripe_public_key,
        "client_secret":intent.client_secret,
        "intent":intent,
    }
    return render(request, 'checkout/checkout.html', context)

def checkout_success(request, order_number):
    context= context_processors.cart_item(request)
    full_cart_item=context['full_cart_item']
    
    for item in full_cart_item:
        product = get_object_or_404(Product, pk=item.product.id)
        product.stock= product.stock - item.quantity
        product.sold= product.sold + item.quantity
        product.save()
        cart = get_object_or_404(Cart, pk=item.id, user=request.user)
        cart.delete()
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your Order has been Received!\
        Your Order Number is {order.order_number}.\
         A confirmation Email will be sent to {order.email}')
    
    email_subject = 'Contact @essence-hotdeskk'
    email_msg = "Your Order has been Received!. It will be processed and delivered soon."
    email_body = "Hi " + order.first_name + " " + email_msg
    # setup email
    email = EmailMessage(
        email_subject,
        email_body,
        "noreply@essence.com",
        [order.email],
        headers={"Message-ID": "@essence-hotdesk"},
    )
    # send email
    email.send(fail_silently=False)

    context={
        'order':order
    }
        
    return render(request, 'checkout_successful/checkout_successful.html', context)
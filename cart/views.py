from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Cart
from product.models import Product
# Create your views here.
def add_to_cart(request):
    try:
        if request.method == "POST":
            product_id = request.POST['product_id']
            qty = request.POST['qty']
            product = get_object_or_404(Product, pk=product_id)
            
            if product.stock < 1:
                messages.warning(request, 'Failure adding to cart:Out of stock!')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            if request.user.is_authenticated:
                
                # Authenticated user
                cart, created = Cart.objects.get_or_create(user=request.user, product=product)
                cart.quantity = qty
                cart.save()
                messages.success(request, 'Product added to Cart')
            else:
               # Unauthenticated user
                carts = request.session.get('carts', [])                 
                cart_item = next((item for item in carts if item['product_id'] == product_id), None)
                if cart_item:                    
                    cart_item['quantity'] = int(cart_item['quantity']) + int(qty)
                else:                    
                    cart_item = {'product_id': product_id, 'quantity': qty}
                    carts.append(cart_item)
                request.session['carts'] = carts
                messages.success(request, 'Product added to Cart')
                    
    except Exception as e:
        messages.error(request, f'Internal Server Error {e}')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_from_cart(request, product_id):
    try:
        product = get_object_or_404(Product, pk=product_id)
        if request.user.is_authenticated:
            # Authenticated user
            Cart.objects.filter(user=request.user, product=product).delete()
            messages.success(request, 'Product removed from Cart')
        else:
            # Unauthenticated user
            carts = request.session.get('carts', [])
            cart_item = next((item for item in carts if item['product_id'] == product_id), None)
            if cart_item:                    
                carts.remove(cart_item)
            request.session['carts'] = carts
            messages.success(request, 'Product removed from Cart')    
                                
    except Exception as e:
        messages.error(request, 'Internal Server Error')
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart(request):
    cart_items = None
    if request.user.is_authenticated:
        cart_items = []
        cart_items = Cart.objects.filter(user=request.user).order_by('-created_at')
    else:
        carts = request.session.get('carts', [])

        if not carts: 
            return render(request, 'cart/cart.html', {'cart_items': []})

        cart_items = []
        for item in carts:
            if isinstance(item, dict) and 'product_id' in item and 'quantity' in item:
                product = get_object_or_404(Product, pk=item['product_id'])
                cart_items.append({'product': product, 'quantity': item['quantity']})
                
    paginator = Paginator(cart_items, 10)
    page = request.GET.get('page')
    
    try:
        cart_items = paginator.page(page)
    except PageNotAnInteger:
        cart_items = paginator.page(1)
    except EmptyPage:
        cart_items = paginator.page(paginator.num_pages)  
        
    context = {
        'cart_items':cart_items,
    }
    return render(request, 'cart/cart.html', context)

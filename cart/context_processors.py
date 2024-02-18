from .models import Cart
from product.models import Product
 
from django.shortcuts import get_object_or_404
from decimal import Decimal
 
def cart_count(request):
    cart_items = None
    cart_items_count = 0
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_items_count = cart_items.count()
    else:
        carts = request.session.get('carts', [])

        if not carts:
            return {'cart_itmes_count': 0}

        cart_item = []
        for item in carts:
            if isinstance(item, dict) and 'product_id' in item and 'quantity' in item:
                product = get_object_or_404(Product, pk=item['product_id'])
                cart_item.append({'product': product, 'quantity': item['quantity']})
                cart_items_count = len(cart_item)
        
    return {'cart_itmes_count': cart_items_count}

def cart_item(request):
    cart_item = None
    total_price = 0
    if request.user.is_authenticated:
        cart_item = (Cart.objects.filter(user=request.user).order_by('-created_at')[:2])
         # Calculate total price
        total_price = sum(item.quantity * item.product.price for item in cart_item)
        
    else:
        carts = request.session.get('carts', [])

        if not carts:
            return  {'cart_item': []}

        cart_item = []
        for item in carts:
            if isinstance(item, dict) and 'product_id' in item and 'quantity' in item:
                product = get_object_or_404(Product, pk=item['product_id'])
                cart_item.append({'product': product, 'quantity': item['quantity']})
                total_price += Decimal(item['quantity']) * Decimal(product.price)
             
    return {
        'cart_item': cart_item,
        'total_price':total_price
    }
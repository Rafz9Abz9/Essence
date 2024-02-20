from django.shortcuts import render

# Create your views here.
def checkout(request):
    if request.method == 'POST':
        items_and_shipping_price= request.POST['items_and_shipping_price']
        
    context ={
        "items_and_shipping_price":items_and_shipping_price
    }
    return render(request, 'checkout/checkout.html', context)
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')


def wishlist(request):
    return render(request, 'wishlist/wishlist.html')


def checkout(request):
    return render(request, 'checkout/checkout.html')


def cart(request):
    return render(request, 'cart/cart.html')

def faq(request):
    return render(request, 'faq/faq.html')


def custom_404_view(request, exception):
    return render(request, '404/404.html', status=404)
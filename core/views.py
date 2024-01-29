from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'contact/contact.html')

def faq(request):
    return render(request, 'faq/faq.html')
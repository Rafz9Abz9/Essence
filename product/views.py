from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render(request, 'product_list/product_list.html')


def product_details(request, product_id):
    return render(request, 'product_list/product_list.html')
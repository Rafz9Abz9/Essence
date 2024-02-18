from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name='cart'),
    path('cart/add/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<product_id>', views.remove_from_cart, name='remove_from_cart'),
]
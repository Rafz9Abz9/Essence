from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<product_id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<product_id>', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('checkout', views.checkout, name='checkout'),
    path('faq', views.faq, name='faq'),
]

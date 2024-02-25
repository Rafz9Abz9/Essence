from django.urls import path
from . import views

#url patterns here
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_successfull/<order_number>', views.checkout_success, name='checkout_success'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('/about-us', views.about, name='about'),
    path('/contact-us', views.contact, name='contact'),
    path('/faq', views.faq, name='faq'),
]

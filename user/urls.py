from django.urls import path
from . import views

urlpatterns = [
    path('auth', views.user_auth_view, name='user_auth'),
    path('profile', views.user_profile, name='user_profile'),
]

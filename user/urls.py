from django.urls import path
from . import views

urlpatterns = [
    path('auth-page', views.user_auth_view, name='user_auth'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.user_profile, name='user_profile'),
]

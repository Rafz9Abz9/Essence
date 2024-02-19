from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

from .guard import AuthenticatedRedirectMiddleware

urlpatterns = [
    path('auth-page', AuthenticatedRedirectMiddleware(views.user_auth_view), name='user_auth'),
    path('register', AuthenticatedRedirectMiddleware(views.register), name='register'),
    path('login', AuthenticatedRedirectMiddleware(views.login_view), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('profile', login_required(views.user_profile), name='user_profile'),
    path('profile/update-info', views.update_user_info, name='update_user_info'),
    path('profile/change-password', views.change_password, name='change_password'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_auth_view, name='user_auth'),
]

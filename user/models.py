from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_("email address"), unique=True, null=False)
    first_name = models.CharField(_("first name"), max_length=50, blank=True, null=True)
    last_name = models.EmailField(_("last name"), max_length=50, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email


class ShippingAddress(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    phone = models.TextField(max_length=20)
    street_address = models.TextField(max_length=250)
    post_code = models.TextField(max_length=20, blank=True)
    city = models.TextField(max_length=80)
    country = models.TextField(max_length=80)
    
    def __str__(self):
        return f'Shipping Address for {self.user}'
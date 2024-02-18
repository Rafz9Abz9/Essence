from django.db import models
from django.utils import timezone

from user.models import CustomUser
from product.models import Product
# Create your models here.
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')
    created_at = models.DateTimeField(default=timezone.now, blank=True)
     
    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"Wishlist Item for {self.user.email}"
    
   
class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150, default="")
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=250)
    message = models.CharField(max_length=1050)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name
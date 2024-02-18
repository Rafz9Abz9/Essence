from django.db import models
from user.models import CustomUser

# Create your models here.
class NewsletterSubscribers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    email = models.EmailField()
    
    class Meta:
        verbose_name_plural = "NewsletterSubscribers"
        
    def __str__(self):
        return f'Newsletter subscribed by {self.email}'
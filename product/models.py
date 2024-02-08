from django.db import models
from PIL import Image as PilImage
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension

# Create your models here.
def validate_image_content(value):
    try:
        img = PilImage.open(value)
    except PilImage.UnidentifiedImageError:
        raise ValidationError("File is not a valid image.")
    
    
class Category(models.Model):
    name = models.CharField(max_length=25, null=False)
    friendly_name = models.CharField(max_length=50, null=False, default=" ")

    def __str__(self):
        return self.name

class Image(models.Model):
    # Fields to store information about each image
    image_file = models.ImageField(
        upload_to='product_images/',
        validators=[validate_image_file_extension, validate_image_content]
    )
    caption = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.caption 

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.BigIntegerField(default=0, null=False)
    sold = models.BigIntegerField(default=0, null=False)
    is_featured = models.BooleanField(default=False)
    images = models.ManyToManyField('Image', related_name='products', blank=True)


    def __str__(self):
        return self.name
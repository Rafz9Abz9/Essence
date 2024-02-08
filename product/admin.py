from django.contrib import admin
from .models import Category,Product,Image

# Register your models here.
class ProductImageInline(admin.TabularInline):
    model = Product.images.through
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product, ProductAdmin)
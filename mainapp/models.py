from django.db import models


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=96, unique=True)
    description = models.TextField(blank=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

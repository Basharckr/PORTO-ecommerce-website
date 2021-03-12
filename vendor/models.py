from django.db import models
from owner.models import Gender, Category
# Create your models here.




class Products(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=150, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to='products/')


class ExtraImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    extra_image = models.FileField(null=True, blank=True, upload_to='products/')

































    
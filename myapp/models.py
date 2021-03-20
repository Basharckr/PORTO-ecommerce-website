from django.db import models
from vendor.models import Products
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)
    checkedout = models.BooleanField(default=False)


    @property
    def subtotal(self):     
        return self.product_count * self.user_product.product_price

   
class ShipAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=150, null=True, blank=True)
    lastname = models.CharField(max_length=150, null=True, blank=True)
    organization = models.CharField(max_length=200, null=True, blank=True)
    streetaddress = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    state = models.CharField(max_length=150, null=True, blank=True)
    country = models.CharField(max_length=150, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)


class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    user_cart = models.name = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

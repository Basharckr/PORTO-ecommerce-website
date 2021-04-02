from django.db import models
from vendor.models import Products
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    report = models.BooleanField(default=False)
    message = models.CharField(max_length=500, null=True, blank=True)
    image1 = models.FileField(null=True, blank=True, upload_to='myapp/profile_pic/')

    @property
    def imageurl(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url   


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
    select = models.BooleanField(default=False)


class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    user_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ship_id = models.ForeignKey(ShipAddress, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)

from django.db import models
from vendor.models import Products
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=1)


    @property
    def subtotal(self):
        return self.product_count * self.user_product.product_price

    @property
    def granttotal(self):
        user = Cart.objects.filter(id=id)
        for item in user:
            total = self.product_count * self.user_product.product_price

        return self.total
 
from django.db import models
from owner.models import Category
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.IntegerField(null=True, blank=True)
    product_name = models.CharField(max_length=150, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    product_quantity = models.IntegerField(null=True, blank=True)
    product_weight = models.IntegerField(null=True, blank=True)
    proudct_description = models.CharField(
        max_length=500, null=True, blank=True)
    product_value = models.BooleanField(default=True)
    image1 = models.FileField(null=True, blank=True,
                              upload_to='vendor/products/')
    image2 = models.FileField(null=True, blank=True,
                              upload_to='vendor/products/')
    image3 = models.FileField(null=True, blank=True,
                              upload_to='vendor/products/')


    @property
    def offer_price(self):  
        if self.category.valid == True and self.category.category_offer != 0:
            new_price = self.product_price - round((self.product_price * (self.category.category_offer) / 100))
        else:
            new_price = self.product_price

        return new_price

    @property
    def image1url(self):
        try:
            url = self.image1.url
        except:
            url = ''
        return url

    @property
    def image2url(self):
        try:
            url = self.image2.url
        except:
            url = ''
        return url
    @property
    def image3url(self):
        try:
            url = self.image3.url
        except:
            url = ''
        return url

        
class Coupon(models.Model):
    coupon_code = models.CharField(max_length=150, null=True, blank=True)
    coupon_offer = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_offer = models.IntegerField(null=True, blank=True)
    valid = models.BooleanField(default=False)
    
class Coupons(models.Model):
    coupon_code = models.CharField(max_length=150, null=True, blank=True)
    coupon_offer = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
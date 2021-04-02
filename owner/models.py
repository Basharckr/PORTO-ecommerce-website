from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_offer = models.IntegerField(null=True, blank=True)
    valid = models.BooleanField(default=False)
    

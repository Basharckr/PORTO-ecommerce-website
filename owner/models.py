from django.db import models

# Create your models here.

class Gender(models.Model):
    BY_GENDER = (
        ('M', 'Men'),
        ('W', 'Women'),
    )
    gender = models.CharField(max_length = 1, choices=BY_GENDER)



class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
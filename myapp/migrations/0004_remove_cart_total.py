# Generated by Django 2.2.2 on 2021-03-18 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]

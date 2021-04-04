# Generated by Django 2.2.2 on 2021-04-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_products_vendor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(blank=True, max_length=150, null=True)),
                ('coupon_offer', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
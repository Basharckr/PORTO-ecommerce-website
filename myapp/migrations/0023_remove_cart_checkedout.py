# Generated by Django 2.2.2 on 2021-03-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20210320_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='checkedout',
        ),
    ]

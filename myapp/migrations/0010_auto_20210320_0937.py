# Generated by Django 2.2.2 on 2021-03-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20210320_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.CharField(default='Not paid', max_length=100),
        ),
    ]

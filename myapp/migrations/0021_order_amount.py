# Generated by Django 2.2.2 on 2021-03-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_auto_20210320_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
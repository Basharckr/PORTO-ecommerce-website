# Generated by Django 2.2.2 on 2021-03-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_auto_20210325_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='report',
            field=models.BooleanField(default=False),
        ),
    ]

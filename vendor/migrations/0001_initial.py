# Generated by Django 2.2.2 on 2021-03-12 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0004_auto_20210311_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.Category')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.Gender')),
            ],
        ),
    ]

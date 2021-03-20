# Generated by Django 2.2.2 on 2021-03-20 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0007_shipaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='checkedout',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Cart')),
            ],
        ),
    ]

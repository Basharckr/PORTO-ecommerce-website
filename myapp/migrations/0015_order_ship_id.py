# Generated by Django 2.2.2 on 2021-03-20 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_order_ship_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ship_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.ShipAddress'),
        ),
    ]

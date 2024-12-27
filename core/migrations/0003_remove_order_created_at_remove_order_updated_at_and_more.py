# Generated by Django 5.1.4 on 2024-12-07 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_products_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

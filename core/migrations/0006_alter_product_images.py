# Generated by Django 5.1.4 on 2024-12-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_products_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
    ]

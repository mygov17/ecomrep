# Generated by Django 5.1.4 on 2024-12-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_products_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
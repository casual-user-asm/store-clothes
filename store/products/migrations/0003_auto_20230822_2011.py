# Generated by Django 3.2.13 on 2023-08-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
    ]

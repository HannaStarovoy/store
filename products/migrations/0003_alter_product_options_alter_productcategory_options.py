# Generated by Django 4.2.11 on 2024-04-11 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]

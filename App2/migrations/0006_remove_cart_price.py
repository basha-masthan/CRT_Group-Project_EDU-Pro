# Generated by Django 5.0.6 on 2024-08-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0005_cart_usr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
    ]

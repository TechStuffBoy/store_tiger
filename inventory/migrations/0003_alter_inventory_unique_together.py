# Generated by Django 3.2.13 on 2022-06-30 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20220630_0253'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('sku', 'product_name')},
        ),
    ]

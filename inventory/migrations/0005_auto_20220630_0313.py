# Generated by Django 3.2.13 on 2022-06-30 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventory_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.2 on 2023-10-09 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_remove_cartitem_subtotal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('created_at',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]

# Generated by Django 4.0.4 on 2023-04-18 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0006_quotation_item_orders_alter_quotation_item_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='item_orders',
        ),
        migrations.AlterField(
            model_name='quotation',
            name='item_bought',
            field=models.JSONField(max_length=255),
        ),
    ]

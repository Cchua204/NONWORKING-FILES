# Generated by Django 4.2.3 on 2023-07-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0003_delete_member_quotation_item_bought'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='order_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-22 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0002_rename_quotations_quotation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.AddField(
            model_name='quotation',
            name='item_bought',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-20 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotations', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quotations',
            new_name='Quotation',
        ),
    ]

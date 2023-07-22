# Generated by Django 4.2.3 on 2023-07-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0005_product_tags_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Charles_Chua_selfie.jpg', null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.0 on 2021-12-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_users_product_cr_on_product_cr_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
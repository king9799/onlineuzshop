# Generated by Django 4.0 on 2021-12-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cr_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cr_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cr_up',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='cr_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='cr_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

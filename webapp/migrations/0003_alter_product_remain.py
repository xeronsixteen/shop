# Generated by Django 4.0.6 on 2022-07-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_remaining_amount_product_remain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='remain',
            field=models.PositiveIntegerField(verbose_name='remain'),
        ),
    ]
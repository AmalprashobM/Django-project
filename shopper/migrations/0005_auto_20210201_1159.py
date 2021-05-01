# Generated by Django 3.1.5 on 2021-02-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0004_shipping_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='item_id',
            field=models.UUIDField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipping',
            name='shop_id',
            field=models.UUIDField(default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.5 on 2021-01-31 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0003_shipping'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1.5 on 2021-02-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0005_auto_20210201_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
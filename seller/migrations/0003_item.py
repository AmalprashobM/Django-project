# Generated by Django 3.1.5 on 2021-01-19 19:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20210120_0116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('discription', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('shop_id', models.UUIDField()),
            ],
        ),
    ]

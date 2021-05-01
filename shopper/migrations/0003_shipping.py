# Generated by Django 3.1.5 on 2021-01-30 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopper', '0002_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-19 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_itempicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempicture',
            name='img_url',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
    ]
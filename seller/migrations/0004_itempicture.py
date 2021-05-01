# Generated by Django 3.1.5 on 2021-01-19 21:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.UUIDField(default=uuid.uuid4)),
                ('img_url', models.CharField(max_length=255)),
            ],
        ),
    ]

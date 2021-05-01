from django.db import models
import uuid

# Create your models here.
class shop(models.Model):
    shop_id =models.UUIDField(default=uuid.uuid4,unique=True)
    name =models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    logo = models.ImageField(max_length=255,null=True)
    user_id = models.IntegerField()

class Item(models.Model):
    item_id =models.UUIDField(default=uuid.uuid4,unique=True)
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=255)
    price =models.FloatField()
    shop_id = models.UUIDField()


class ItemPicture(models.Model):
    item_id = models.UUIDField(default=uuid.uuid4)
    img_url = models.FileField(max_length=255)



    
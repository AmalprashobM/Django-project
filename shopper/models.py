from django.db import models

# Create your models here.
class PageView(models.Model):
    item_id = models.UUIDField()
    timestamp = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    item_id = models.UUIDField()
    user_id = models.IntegerField()
    quantity = models.IntegerField()

class Shipping(models.Model):
    firstname = models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    mobile =models.IntegerField()
    address=models.CharField(max_length=255)
    state =models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    pincode =models.IntegerField()
    quantity=models.IntegerField()
    shop_id = models.UUIDField()
    item_id = models.UUIDField()
    timestamp = models.DateTimeField(auto_now=True)





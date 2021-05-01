from django.db import models

# Create your models here.
class createuser(models.Model):
    userid =models.CharField(max_length=100)
    role = models.CharField(max_length=100)

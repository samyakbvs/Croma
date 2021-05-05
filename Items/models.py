from django.db import models
from django.db.models.signals import post_save
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200,unique=True)
    description = models.CharField(max_length=200)
    stock = models.BigIntegerField()

    def __str__(self):
        return self.name

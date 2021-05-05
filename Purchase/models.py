from django.db import models
from Items.models import Item
from django.db.models.signals import post_init

# Create your models here.

class Suppliers(models.Model):
    name = models.CharField(max_length=264)
    address = models.CharField(max_length=264)
    gst = models.CharField(max_length=264)

class SupplierInvoice(models.Model):
    Name = models.ForeignKey(Suppliers,on_delete=models.CASCADE)
    Inv_num = models.BigIntegerField(unique=True)
    Date = models.DateField()
    Doc_num = models.BigIntegerField()
    Doc_date = models.DateField()
    Mode = models.CharField(max_length=264)
    Raw_amount = models.BigIntegerField(default=0)
    Final_amount = models.BigIntegerField(default=0)

    def subtracted(self):
        return (self.Raw_amount - self.Final_amount)

    def __str__(self):
        return str(self.Inv_num)


class ItemsPurchased(models.Model):

    name = models.ForeignKey(Item,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,default="0")
    quantity = models.BigIntegerField()
    quantity_free = models.BigIntegerField()
    price = models.BigIntegerField()
    sgst = models.BigIntegerField()
    cgst = models.BigIntegerField()
    discount = models.BigIntegerField()
    invoice = models.ForeignKey(SupplierInvoice, on_delete=models.CASCADE,related_name="items")
    amount = models.BigIntegerField(default=0)

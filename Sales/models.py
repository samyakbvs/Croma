from django.db import models
from Items.models import Item
# Create your models here.

class BuyerInvoice(models.Model):
    Name = models.CharField(max_length=264)
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


class ItemsSold(models.Model):
    name = models.ForeignKey(Item,on_delete=models.CASCADE)
    code = models.CharField(max_length=264,default="0")
    quantity = models.BigIntegerField()
    price = models.BigIntegerField()
    sgst = models.BigIntegerField()
    cgst = models.BigIntegerField()
    discount = models.BigIntegerField()
    invoice = models.ForeignKey(BuyerInvoice, on_delete=models.CASCADE,related_name="items")
    amount = models.BigIntegerField(default=0)

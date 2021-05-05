from django.contrib import admin

# Register your models here.
from Items.models import Item
from Purchase.models import SupplierInvoice,ItemsPurchased
from Sales.models import BuyerInvoice,ItemsSold
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ItemsPurchasedInline(admin.TabularInline):
    model = ItemsPurchased
    can_delete = False
    verbose_name_plural = 'Items Purchased'

class SupplierInvoiceAdmin(admin.ModelAdmin):
    inlines = (ItemsPurchasedInline,)

class ItemsSoldInline(admin.TabularInline):
    model = ItemsSold
    can_delete = False
    verbose_name_plural = 'Items Purchased'

class BuyerInvoiceAdmin(admin.ModelAdmin):
    inlines = (ItemsSoldInline,)


admin.site.register(Item)
admin.site.register(SupplierInvoice,SupplierInvoiceAdmin)
admin.site.register(BuyerInvoice,BuyerInvoiceAdmin)

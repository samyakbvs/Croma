from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
from . models import ItemsPurchased,SupplierInvoice,Suppliers
from Items.models import Item

# Create your views here.

class ViewPurchases(APIView):
    def get(self,request):
        Purchases_all = SupplierInvoice.objects.all()
        return render(request,'Purchase/viewPurchases.html',{'Purchases_all':Purchases_all})

class ItemPurchased(APIView):
    def get(self,request):
        all_suppliers = Suppliers.objects.all()
        return render(request,'Purchase/purchase.html',{'all_suppliers':all_suppliers})
    def post(self,request):
        supplier_name = request.POST['Name']
        supplier = Suppliers.objects.get(name=supplier_name)
        Name = supplier
        Inv_num = request.POST['Inv_num']
        Date = request.POST['Date']
        Doc_num = request.POST['Doc_num']
        Doc_date = request.POST['Doc_date']
        Mode = request.POST['Mode']
        Invoice = SupplierInvoice(Name=Name,Inv_num=Inv_num,Date=Date,Doc_num=Doc_num,Doc_date=Doc_date,Mode=Mode)
        Invoice.save()

        return redirect('viewSupplierInvoice',Inv_num)

class ViewInvoice(APIView):
    def get(self, request, Inv_num):
        Items = Item.objects.all()
        Invoice = SupplierInvoice.objects.get(Inv_num=Inv_num)
        all_suppliers = Suppliers.objects.all()
        return render(request,'Purchase/viewInvoice.html',{'Invoice':Invoice,'Items':Items,'all_suppliers':all_suppliers})
    def post(self,request,Inv_num):
        Invoice = SupplierInvoice.objects.get(Inv_num=Inv_num)
        supplier_name = request.POST['Name']
        supplier = Suppliers.objects.get(name=supplier_name)
        Invoice.Name = supplier
        Invoice.Inv_num = request.POST['Inv_num']
        # Invoice.Date = request.POST['Date']
        Invoice.Doc_num = request.POST['Doc_num']
        # Invoice.Doc_date = request.POST['Doc_date']
        Invoice.Mode = request.POST['Mode']
        Invoice.save()
        return redirect('viewSupplierInvoice',Inv_num)

class PurchaseItem(APIView):
    def post(self, request, Inv_num):
        print(request.POST['code'])
        item = Item.objects.get(code=request.POST['code'])
        invoice = SupplierInvoice.objects.get(Inv_num=Inv_num)
        code = request.POST['code']
        quantity = int(request.POST['quantity'])
        free_quantity = int(request.POST['free_quantity'])
        price = int(request.POST['price'])
        discount = int(request.POST['discount'])
        cgst = int(request.POST['cgst'])
        sgst = int(request.POST['sgst'])
        raw_amount = price*quantity*(1+cgst/100)*(1+sgst/100)
        amount = price*quantity*(1+cgst/100)*(1+sgst/100)*(1-discount/100)
        invoice.Raw_amount += raw_amount
        invoice.Final_amount += amount
        invoice.save()
        item_purchased = ItemsPurchased(invoice=invoice,code=code,name=item,quantity=quantity,quantity_free=free_quantity,price=price,discount=discount,cgst=cgst,sgst=sgst,amount=amount)
        item_purchased.save()
        item.stock += quantity+free_quantity
        item.save()
        return redirect('viewSupplierInvoice',Inv_num)

class FilterInvoices(APIView):
    def post(self, request):
        Purchases_all = SupplierInvoice.objects.filter(Inv_num__icontains=request.POST['query'])
        return render(request,'Purchase/viewPurchases.html',{'Purchases_all':Purchases_all})

class DeleteItemPurchased(APIView):
    def post(self, request, id):
        item_purchased = ItemsPurchased.objects.get(id=id)
        invoice = item_purchased.invoice
        item = item_purchased.name
        item.stock -= item_purchased.quantity + item_purchased.quantity_free
        item.save()
        item_purchased.delete()
        print("post")
        return redirect('viewSupplierInvoice',invoice.Inv_num)

class EditItemPurchased(APIView):
    def get(self,request,id):
        item_purchased = ItemsPurchased.objects.get(id=id)
        return render(request,'Purchase/editItemPurchased.html',{'item_purchased':item_purchased})
    def post(self,request,id):
        item_purchased = ItemsPurchased.objects.get(id=id)
        diff_quantity = (int(request.POST['quantity'])+int(request.POST['quantity_free'])) - (item_purchased.quantity + item_purchased.quantity_free)
        print(diff_quantity)
        item_purchased.name.stock += diff_quantity
        item_purchased.name.save()
        item_purchased.price = request.POST['price']
        item_purchased.discount = request.POST['discount']
        item_purchased.cgst = int(request.POST['cgst'])
        item_purchased.sgst = int(request.POST['sgst'])
        item_purchased.quantity = request.POST['quantity']
        item_purchased.quantity_free = request.POST['quantity_free']
        item_purchased.amount = int(request.POST['price'])*int(request.POST['quantity'])*(1+int(request.POST['cgst'])/100)*(1+int(request.POST['sgst'])/100)*(1-int(request.POST['discount'])/100)
        item_purchased.save()
        return redirect('viewSupplierInvoice',item_purchased.invoice.Inv_num)

class ViewSuppliers(APIView):
    def get(self,request):
        all_suppliers = Suppliers.objects.all()
        return render(request, 'Purchase/viewSuppliers.html', {'all_suppliers':all_suppliers})

class AddSuppliers(APIView):
    def get(self,request):
        return render(request,'Purchase/addSuppliers.html')
    def post(self,request):
        Supplier = Suppliers(name=request.POST['name'],address=request.POST['address'],gst=request.POST['gstin'])
        Supplier.save()
        all_suppliers = Suppliers.objects.all()
        return render(request,'Purchase/viewSuppliers.html',{'all_suppliers':all_suppliers})
class DeleteSuppliers(APIView):
    def post(self,request,id):
        supplier = Suppliers.objects.get(id=id)
        supplier.delete()
        all_suppliers = Suppliers.objects.all()
        return render(request, 'Purchase/viewSuppliers.html', {'all_suppliers':all_suppliers})
class editSuppliers(APIView):
    def get(self,request,id):
        Supplier = Suppliers.objects.get(id=id)
        return render(request, 'Purchase/editSuppliers.html', {'Supplier':Supplier})
    def post(self,request,id):
        Supplier = Suppliers.objects.get(id=id)
        Supplier.name = request.POST['name']
        Supplier.address = request.POST['address']
        Supplier.gst = request.POST['gstin']
        Supplier.save()
        all_suppliers = Suppliers.objects.all()
        return render(request, 'Purchase/viewSuppliers.html', {'all_suppliers':all_suppliers})

from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.contrib import auth
from . models import ItemsSold,BuyerInvoice
from Items.models import Item

# Create your views here.

class ViewSales(APIView):
    def get(self,request):
        Sales_all = BuyerInvoice.objects.all()
        return render(request,'Sales/viewSales.html',{'Sales_all':Sales_all})

class ItemSold(APIView):
    def get(self,request):
        return render(request,'Sales/sales.html')
    def post(self,request):
        Name = request.POST['Name']
        Inv_num = request.POST['Inv_num']
        Date = request.POST['Date']
        Doc_num = request.POST['Doc_num']
        Doc_date = request.POST['Doc_date']
        Mode = request.POST['Mode']
        Invoice = BuyerInvoice(Name=Name,Inv_num=Inv_num,Date=Date,Doc_num=Doc_num,Doc_date=Doc_date,Mode=Mode)
        Invoice.save()

        return redirect('viewBuyerInvoice',Inv_num)

class ViewInvoice(APIView):
    def get(self, request, Inv_num):
        Items = Item.objects.all()
        Invoice = BuyerInvoice.objects.get(Inv_num=Inv_num)
        return render(request,'Sales/viewInvoice.html',{'Invoice':Invoice,'Items':Items})

    def post(self,request,Inv_num):
        Invoice = BuyerInvoice.objects.get(Inv_num=Inv_num)
        Invoice.Name = request.POST['Name']
        Invoice.Inv_num = request.POST['Inv_num']
        # Invoice.Date = request.POST['Date']
        Invoice.Doc_num = request.POST['Doc_num']
        # Invoice.Doc_date = request.POST['Doc_date']
        Invoice.Mode = request.POST['Mode']
        Invoice.save()
        return redirect('viewBuyerInvoice',Inv_num)

class SellItem(APIView):
    def post(self, request, Inv_num):
        print(request.POST['code'])
        item = Item.objects.get(code=request.POST['code'])
        invoice = BuyerInvoice.objects.get(Inv_num=Inv_num)
        code = request.POST['code']
        quantity = int(request.POST['quantity'])
        price = int(request.POST['price'])
        discount = int(request.POST['discount'])
        cgst = int(request.POST['cgst'])
        sgst = int(request.POST['sgst'])
        raw_amount = price*quantity*(1+cgst/100)*(1+sgst/100)
        amount = price*quantity*(1+cgst/100)*(1+sgst/100)*(1-discount/100)
        invoice.Final_amount += amount
        invoice.Raw_amount += raw_amount
        invoice.save()
        item_sold = ItemsSold(invoice=invoice,code=code,name=item,quantity=quantity,price=price,discount=discount,cgst=cgst,sgst=sgst,amount=amount)
        item_sold.save()
        item.stock -= quantity
        item.save()
        return redirect('viewBuyerInvoice',Inv_num)

class FilterInvoices(APIView):
    def post(self, request):
        Sales_all = BuyerInvoice.objects.filter(Inv_num__icontains=request.POST['query'])
        return render(request,'Sales/viewSales.html',{'Sales_all':Sales_all})

class DeleteItemSold(APIView):
    def post(self, request, id):
        item_sold = ItemsSold.objects.get(id=id)
        invoice = item_sold.invoice
        item = item_sold.name
        item.stock += item_sold.quantity
        item.save()
        item_sold.delete()
        print("post")
        return redirect('viewBuyerInvoice',invoice.Inv_num)

class EditItemSold(APIView):
    def get(self,request,id):
        item_sold = ItemsSold.objects.get(id=id)
        return render(request,'Sales/editItemSold.html',{'item_sold':item_sold})
    def post(self,request,id):
        item_sold = ItemsSold.objects.get(id=id)
        diff_quantity = (int(request.POST['quantity'])) - (item_sold.quantity)
        item_sold.name.stock -= diff_quantity
        item_sold.name.save()
        item_sold.price = request.POST['price']
        item_sold.discount = request.POST['discount']
        item_sold.cgst = int(request.POST['cgst'])
        item_sold.sgst = int(request.POST['sgst'])
        item_sold.quantity = request.POST['quantity']
        item_sold.amount = int(request.POST['price'])*int(request.POST['quantity'])*(1+int(request.POST['cgst'])/100)*(1+int(request.POST['sgst'])/100)*(1-int(request.POST['discount'])/100)
        item_sold.save()
        return redirect('viewBuyerInvoice',item_sold.invoice.Inv_num)

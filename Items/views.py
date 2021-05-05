from django.shortcuts import render,redirect,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from rest_framework.views import APIView
from django.contrib import auth
from . models import Item
from Purchase.models import ItemsPurchased,SupplierInvoice
from Sales.models import ItemsSold,BuyerInvoice
import pandas as pd
import csv
from django.utils.encoding import smart_str
from io import BytesIO
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum
# Create your views here.

main_list = []

class ItemView(APIView):
    def get(self,request):
        Items_all = Item.objects.all()
        return render(request,'Items/items.html',{'Items_all':Items_all})

class AddItems(APIView):
    def post(self,request):
        name = request.POST['name']
        code = request.POST['code']
        description = request.POST['description']
        stock = request.POST['stock']
        new_item = Item(name=name,code=code,description=description,stock=stock)
        new_item.save()
        Items_all = Item.objects.all()
        return render(request,'Items/items.html',{'Items_all':Items_all})

class Reports(APIView):
    def get(self,request):
        return render(request,'Items/reports.html')
    def post(self,request):
        global main_list
        main_list = []
        supplier_invoices = SupplierInvoice.objects.filter(Date__range=[str(request.POST['start_date']), str(request.POST['end_date'])])
        buyer_invoices = BuyerInvoice.objects.filter(Date__range=[str(request.POST['start_date']), str(request.POST['end_date'])])
        items_purchased = []
        items_sold = []
        for supplier_invoice in supplier_invoices:
            for item in supplier_invoice.items.all():
                items_purchased.append(item)
        for buyer_invoice in buyer_invoices:
            for item in buyer_invoice.items.all():
                items_sold.append(item)

        for item in Item.objects.all():
            temp = [0,0,0,0,0]
            temp[0]=item.name
            temp[1]=item.code
            for purchased_item in items_purchased:
                if purchased_item.name == item:
                    temp[2] += purchased_item.amount
            for sold_item in items_sold:
                if sold_item.name == item:
                    temp[3] += sold_item.amount
            temp[4] = temp[3] - temp[2]
            main_list.append(temp)
        # print(main_list)

        return render(request,'Items/reports.html', {'main_list':main_list})

class ExportReports(APIView):
    def post(self,request):
        global main_list
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Report.csv"'
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))

        writer.writerow([
        smart_str(u"Name"),
        smart_str(u"Code"),
        smart_str(u"Purchase Cost"),
        smart_str(u"Sales Revenue"),
        smart_str(u"Profit and Loss"),
        ])
        for item in main_list:
            writer.writerow([
            smart_str(item[0]),
            smart_str(item[1]),
            smart_str(item[2]),
            smart_str(item[3]),
            smart_str(item[4]),
            ])
        return response

class PDF(APIView):
    def post(self,request):
        global main_list
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Report.pdf"'
        response['Content-Transfer-Encoding'] = 'binary'

        html_string=render_to_string('Items/pdf.html',{'main_list':main_list})
        html = HTML(string=html_string)
        result = html.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output=open(output.name,'rb')
            response.write(output.read())

        return response

"""Croma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ViewPurchases.as_view(),name='viewPurchases'),
    path('create/', views.ItemPurchased.as_view(),name='itemPurchased'),
    path('viewInvoice/<int:Inv_num>', views.ViewInvoice.as_view(),name='viewSupplierInvoice'),
    path('purchaseItem/<int:Inv_num>', views.PurchaseItem.as_view(),name='purchaseItem'),
    path('filterSupplierInvoice', views.FilterInvoices.as_view(), name='filterSupplierInvoice' ),
    path('deleteItemPurchased/<str:id>', views.DeleteItemPurchased.as_view(), name='deleteItemPurchased' ),
    path('editItemPurchased/<str:id>', views.EditItemPurchased.as_view(), name='editItemPurchased' ),
    path('addSuppliers/', views.AddSuppliers.as_view(), name='addSuppliers' ),
    path('viewSuppliers/', views.ViewSuppliers.as_view(), name='viewSuppliers' ),
    path('deleteSuppliers/<str:id>', views.DeleteSuppliers.as_view(), name='deleteSuppliers' ),
    path('editSuppliers/<str:id>', views.editSuppliers.as_view(), name='editSuppliers' ),

]

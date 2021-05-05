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
    path('', views.ViewSales.as_view(),name='viewSales'),
    path('create/', views.ItemSold.as_view(),name='itemSold'),
    path('viewInvoice/<int:Inv_num>', views.ViewInvoice.as_view(),name='viewBuyerInvoice'),
    path('sellItem/<int:Inv_num>', views.SellItem.as_view(),name='sellItem'),
    path('filterBuyerInvoice/', views.FilterInvoices.as_view(), name='filterBuyerInvoice' ),
    path('deleteItemSold/<str:id>', views.DeleteItemSold.as_view(), name='deleteItemSold' ),
    path('editItemSold/<str:id>', views.EditItemSold.as_view(), name='editItemSold' ),



]

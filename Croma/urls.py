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
from django.urls import path,include
from Account import urls as Account_urls
from Items import urls as Items_urls
from Purchase import urls as Purchase_urls
from Sales import urls as Sales_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Account_urls)),
    path('items/',include(Items_urls)),
    path('purchase/',include(Purchase_urls)),
    path('sales/',include(Sales_urls)),
]

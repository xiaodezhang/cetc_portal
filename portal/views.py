# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portal/home.html')

def succeedproduct(request):
    return render(request,'portal/succeed_product.html')

def sht_info(request):
    return render(request,'portal/sht_info.html')

def product_service(request):
    return render(request,'portal/product_service.html')

def municipal(request):
    return render(request,'portal/municipal.html')

def gis(request):
    return render(request,'portal/gis.html')

def news_center(request):
    return render(request,'portal/news_center.html')

def job_take(request):
    return render(request,'portal/job_take.html')

def contact_us(request):
    return render(request,'portal/contact_us.html')


def news_list(request,news_date):
    return render(request,'portal/'+news_date+'.html')

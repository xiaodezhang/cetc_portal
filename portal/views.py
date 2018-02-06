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

def sht_culture(request):
    return render(request,'portal/sht_culture.html')

def product_service(request):
    return render(request,'portal/product_service.html')

def municipal(request):
    return render(request,'portal/municipal.html')

def pip_network(request):
    return render(request,'portal/pip_network.html')

def sht_archevement(request):
    return render(request,'portal/sht_archevement.html')

def sht_summary(request):
    return render(request,'portal/sht_summary.html')

def city_lighting(request):
    return render(request,'portal/city_lighting.html')

def smart_city(request):
    return render(request,'portal/smart_city.html')

def smart_pole(request):
    return render(request,'portal/smart_pole.html')


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

def job_list(request,job_number):
    return render(request,'portal/job_take_'+job_number+'.html')

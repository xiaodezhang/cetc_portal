from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
        url(r'^$',views.home,name = 'home'),
        url(r'^home',views.home,name = 'home'),
        url(r'^product_service',views.product_service,name = 'product_service'),
        url(r'^sht_info',views.sht_info,name = 'sht_info'),
        url(r'^succeedproduct',views.succeedproduct,name = 'succeedproduct'),
        url(r'^municipal',views.municipal,name = 'municipal'),
        url(r'^smart_city',views.smart_city,name = 'smart_city'),
        url(r'^smart_pole',views.smart_pole,name = 'smart_pole'),
        url(r'^sht_summary',views.sht_summary,name = 'sht_summary'),
        url(r'^sht_culture',views.sht_culture,name = 'sht_culture'),
        url(r'^sht_archevement',views.sht_archevement,name = 'sht_archevement'),
        url(r'^pip_network',views.pip_network,name = 'pip_network'),
        url(r'^city_lighting',views.city_lighting,name = 'city_lighting'),
        url(r'^gis',views.gis,name = 'gis'),
        url(r'^job_take',views.job_take,name = 'job_take'),
        url(r'^news_center',views.news_center,name = 'news_center'),
        url(r'^contact_us',views.contact_us,name = 'contact_us'),
        path(r'news_list/<str:news_date>',views.news_list,name = 'news_list'),
        path(r'job_list/<str:job_number>',views.job_list,name = 'job_list'),
] 


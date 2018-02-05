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
        url(r'^gis',views.gis,name = 'gis'),
        url(r'^job_take',views.job_take,name = 'job_take'),
        url(r'^news_center',views.news_center,name = 'news_center'),
        url(r'^contact_us',views.contact_us,name = 'contact_us'),
        path(r'news_list/<str:news_date>',views.news_list,name = 'news_list'),
] 


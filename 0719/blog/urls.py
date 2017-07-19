#coding:utf-8

from django.conf.urls import url  #导入URL模块
from . import views    #从当前目录导入views模块

app_name = 'blog'

#网址和处理函数
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url('contact', views.contact, name='contact'),
    url('about', views.about, name='about'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category')
]
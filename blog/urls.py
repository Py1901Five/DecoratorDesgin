from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import *
# 全文搜索
from haystack.views import SearchView


app_name = 'blog'

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^$', login, name='login'),
    url(r'^public/$', public, name='public'),
    url(r'^total/$', total, name='total'),
    url(r'^single/(\d+)/$', single, name='single'),
    url(r'^see/$', see, name='see'),
    url(r'^large_total/$', large_total, name='large_total'),
    # 全文搜索，调用第三方库中的视图函数
    url(r'^search/$', SearchView(), name='search'),

]

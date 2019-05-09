from django.conf.urls import url
from . import views

app_name = 'shop'
urlpatterns = [
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shop_single/(\d+)/$', views.shop_single, name='shop_single'),
    url(r'^shopping_cart/$', views.shopping_cart, name='shopping_cart'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^category/(\d+)/$', views.category, name='category'),
    url(r'^tag/(\d+)/$', views.tag, name='tag'),
    url(r'^add_cart/(\d+)/$', views.add_cart, name='add_cart'),
    url(r'^price_filter/$', views.price_filter, name='price_filter'),
    url(r'^review/(\d+)/$', views.review, name='review'),
    url(r'^remove_product/(\d+)/$', views.remove_product, name='remove_product'),
    url(r'^search/$', views.search, name='search'),
]

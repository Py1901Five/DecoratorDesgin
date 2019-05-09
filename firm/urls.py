from django.conf.urls import url
from . import views

app_name = 'firm'


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^pricing/$',views.pricing,name='pricing'),
    url(r'^question/$', views.faqs,name='question'),
    url(r'^team-single/(\d+)/$',views.team_single,name='team-single'),
    url(r'^team/$',views.team,name='team'),
    url(r'^about/$',views.about,name='about'),
]
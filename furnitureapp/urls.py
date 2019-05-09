from django.conf.urls import url
from . import views

app_name = 'furnitureapp'
urlpatterns = [
    url('^$', views.portfoli, name='portfoli'),
    url(r'^defalut/(\d+)/$', views.defalut, name='defalut'),
    url(r'^singletwo/(\d+)/(\d+)/$', views.singletwo, name='singletwo'),
    url(r'^fullwidth/$',views.fullwidth, name='fullwidth'),
    url(r'^pictext/$',views.pictext,name='pictext'),
    url(r'^sendemail/$',views.sendemail,name='sendemail')
]

from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse


# Create your views here.
def getpage(request, objectlist):
    paginatorlist = Paginator(objectlist, 9)
    pagenum = request.GET.get("page")
    pagenum = 1 if pagenum == None else pagenum
    page = paginatorlist.page(pagenum)
    return page


def portfoli(request):
    classify = Classify.objects.all()
    indeximg = Furniture.objects.all()
    return render(request, 'furnitureapp/portfolio-default.html', {'classifies': classify, 'indeximgs': indeximg})


def defalut(request, id):
    indeximg = Furniture.objects.get(pk=id)
    furnitureinfo = indeximg.furnitureinfo_set.all()
    furnitureimg = indeximg.furnitureimg_set.all()
    return render(request, 'furnitureapp/portfolio-single-one.html',
                  {'furnitureInfo': furnitureinfo, 'furnitureimg': furnitureimg})


def singletwo(request, id, fid):
    articles = FurnitureInfo.objects.get(pk=id)
    slp = FullWidth.objects.get(pk=fid)
    img = SingTwo.objects.filter(sfor=slp).all()
    return render(request, 'furnitureapp/portfolio-single-two.html', {'pics': img, 'articles': articles})


def fullwidth(request):
    classify = Classify.objects.all()
    wpic = FullWidth.objects.all()
    return render(request, 'furnitureapp/portfolio-fullwidth.html', {'classify': classify, 'wpics': wpic})


def pictext(request):
    classify = Classify.objects.all()
    textimg = TextPic.objects.all()
    page = getpage(request, textimg)
    return render(request, 'furnitureapp/portfolio-with-text.html', {'classify': classify, 'textimg': page, 'page': page})


def sendemail(request):
    if request.method == 'GET':
        return render(request, 'furnitureapp/contact.html')
    elif request.method == 'POST':
        userinfo = UserInfo(subject=request.POST['subject'], name=request.POST['username'], email=request.POST['email'],
                            phonenumber=request.POST['phone'], message=request.POST['message'])
        userinfo.save()
        email = userinfo.email
        send_mail("we find out you message. later send you",
                  "There are many variations off +1800 854 5864 available, "
                  "but the majority have ut suffered alterattions in some"
                  " forms by injected humour looks events slightly "
                  "seds believable ut seds do eiusmod tempor incididunt labore.",
                  settings.DEFAULT_FROM_EMAIL, [email])
        return HttpResponse('sended')

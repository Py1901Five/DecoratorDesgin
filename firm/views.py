from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import *
from .forms import PotentialForm
# Create your views here.


def index(request):
    services = Service.objects.all()
    traits = Trait.objects.all()
    stylists = Stylist.objects.all()
    shoplists = ShopList.objects.all()
    data = {'services':services,'traits':traits,'stylists':stylists,'shoplists':shoplists}
    return render(request,'firm/index.html',data)


def pricing(request):
    pricings = Pricing.objects.all()
    return render(request,'firm/pricing.html',{'pricings':pricings})


def faqs(request):
    if request.method == 'GET':
        questions = Question.objects.all().order_by('-id')[:6]
        return render(request,'firm/faqs.html',{'questions':questions})
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['number']
        question = request.POST['message']
        print(username,email,phone,question)
        user = Potential()
        user.username = username
        user.email = email
        user.phone = phone
        user.question = question
        user.save()
        return redirect(reverse("firm:question"))


def team_single(request,id):
    parents = Team.objects.all()
    parent = Team.objects.get(pk=id)
    team_details = Team.objects.get(pk=id).education_set.all()
    ids = int(id)
    ss = {'parents':parents,'details':team_details,'id':ids,'user':parent}
    return render(request,'firm/team-single.html',ss)


def team(request):
    team_list = Team.objects.all()
    return render(request,'firm/team.html',{'team_list':team_list})


def about(request):
    parents = Team.objects.all()[:4]
    return render(request,'firm/about.html',{'parents':parents})



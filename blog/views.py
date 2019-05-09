from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from .models import *
from django.core.paginator import Paginator


def register(request):
    """注册"""
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        jj = request.POST['jj']
        headerimage = request.FILES['headerimage']
        UserSell.objects.create(uName=name, uheaderImg=headerimage, uPwd=pwd, uBrief=jj)
        return redirect(reverse('blog:login'))
    return render(request, 'blog/register.html')


def login(request):
    """login"""
    if request.method == 'POST':
        name = request.POST['name']
        pwd = request.POST['pwd']
        us = UserSell.objects.filter(uName=name, uPwd=pwd)
        if len(us) > 0:
            # 设置session
            request.session['u'] = us[0].id
            return redirect(reverse('blog:public'))
    return render(request, 'blog/login.html')


def public(request):
    """发表文章"""
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        type = Type.objects.get(pk=request.POST['type'])
        tags = request.POST['tags']
        img = request.FILES['articleImage']

        ari = Article()
        ari.aBackgroundImage = img
        ari.aTitle = title
        ari.aContent = content
        ari.aType = type
        ari.aAuthor = UserSell.objects.get(pk=int(request.session['u']))
        ari.save()
        for t in tags:
            ari.aTag.add(int(t))
        ari.save()
    # 查询分类，传入内容
    types = Type.objects.all()
    tags = Tag.objects.all()
    para = {
        'types': types,
        'tags': tags,
    }
    return render(request, 'blog/public_article.html', para)


def search_resource():
    """
    查询共有资源
    :return: {'articles': types,
        'tags': tags,
        'types': articles,}
    """
    types = Type.objects.all()
    tags = Tag.objects.all()
    articles = Article.objects.all()
    # 归档
    t_set = set()
    for a in articles:
        time = a.aPublicTime.month
        t_set.add('2019-'+str(time))
    # i = 1
    # for m in t_set:
    #     if i < 5:
    #         a = []
    #         a.append('2019-'+str(m))


    # 热门文章
    hot_arls = articles.order_by('-aReadNum')[:3]
    para = {
        'articles': articles,
        'tags': tags,
        'types': types,
        'hot_arls': hot_arls,
        'guidang': t_set,
    }
    return para


def total(request):
    """
    总览页
    :param request:
    :return:
    """
    para = search_resource()
    pindex = request.GET.get('page')
    if pindex is None:
        pindex = 1
    p = Paginator(para['articles'], 6)
    pindex = int(pindex)
    page = p.page(pindex)
    para['articles'] = page.object_list
    para['page'] = page
    para['p'] = p
    return render(request, 'blog/blog.html', para)


def single(request, aid):
    """
    详情页
    :param request:
    :param aid:书的id
    :return:
    """
    arl = Article.objects.get(pk=int(aid))
    # 阅读数加一
    arl.aReadNum += 1
    arl.save()
    coms = arl.comment_set.all()
    para = search_resource()
    para['arl'] = arl
    para['coms'] = coms
    print('.....................................', para)
    return render(request, 'blog/blog-single.html', para)


def see(request):
    part_types = None
    type = request.GET.get('type')
    # 对应类型id
    value = request.GET.get('value')
    if type == 'type':
        part_types = Type.objects.get(pk=int(value)).article_set.all()
    elif type == 'tag':
        part_types = Tag.objects.get(pk=int(value)).article_set.all()
    elif type== 'date':
        year = value[:4]
        month = value[5:]
        part_types = Article.objects.filter(aPublicTime__year=year, aPublicTime__month=month).all()
    para = search_resource()

    p = Paginator(part_types, 6)
    pindex = request.GET.get('page')
    if pindex is None:
        pindex = 1
    pindex = int(pindex)
    page = p.page(pindex)
    para['articles'] = page.object_list
    para['page'] = page
    para['type'] = type
    para['value'] = value
    para['p'] = p
    return render(request, 'blog/blog.html', para)


def large_total(request):
    para = search_resource()
    return render(request, 'blog/blog-large-image.html', para)



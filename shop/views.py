from django.shortcuts import render, redirect, reverse
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage
from django.http import HttpResponse
# Create your views here.


def render_shop(request, products):
    """ 给定产品信息，渲染shop页面 """
    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()
    latest_products = models.Product.objects.all().order_by('pub_date')[0:3]

    # 根据产品数量分页
    limit = 9  # 按每页9条分页
    page_number = 3  # 每页页码数量
    paginator = Paginator(products, limit)
    page_range = None
    if request.method == "GET":
        # 获取 url 后面的 page 参数的值, 首页不显示 page 参数, 默认值是 1
        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        # 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            products = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        finally:
            # 生成当前页页码范围
            if products.number + page_number < products.paginator.num_pages:
                page_range = range(products.number, products.number + page_number)
            else:
                page_range = range(products.number, products.paginator.num_pages)
    print(page_range)
    return render(request, 'shop/shop.html',
                  {'products': products,
                   'categories': categories,
                   'tags': tags,
                   'latest_products': latest_products,
                   'page_range': page_range,
                   })


def shop(request):
    """ 商品页面 """
    products = models.Product.objects.all()
    return render_shop(request, products)


def shop_single(request, product_id):
    """ 商品详情 """
    product = models.Product.objects.get(pk=product_id)
    categories = models.Category.objects.all()
    tags = models.Tag.objects.all()
    latest_products = models.Product.objects.all().order_by('pub_date')[0:3]
    return render(request, 'shop/shop-single.html',
                  {'product': product, 'categories': categories, 'tags': tags, 'latest_products': latest_products})


def shopping_cart(request):
    """ 购物车 """
    user = models.User.objects.get(name=request.session.get('username'))
    cart = user.cart_set.all()

    total_price = 0
    for product in cart:
        total_price += product.product.price * product.quantity

    return render(request, 'shop/shopping-cart.html', {'cart': cart, 'total_price': total_price})


def login(request):
    """ 登录 """
    username = request.POST.get('username')
    pwd = request.POST.get('pwd')
    user = models.User.objects.filter(name=username, pwd=pwd).first()
    if user:
        request.session['username'] = username
        return redirect(to=reverse('shop:shop'))
    else:
        return render(request, 'shop/register.html', {'failed': True})


def register(request):
    """ 注册 """
    if request.method == 'GET':
        return render(request, 'shop/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        models.User.objects.create(name=username, pwd=pwd, email=email)
        return redirect(to=reverse('shop:register'))


def checkout(request):
    """ 支付 """
    if request.method == 'POST':
        # TODO 第三方支付
        return redirect(to=reverse('shop:shop'))
    return render(request, 'shop/checkout.html')


def add_cart(request, product_id):
    """ 添加商品到购物车 """
    product = models.Product.objects.get(pk=product_id)
    user = models.User.objects.get(name=request.session.get('username'))

    try:
        quantity = request.POST.get('quantity')
    except Exception as e:
        models.Cart.objects.create(product=product, user=user)
    else:
        models.Cart.objects.create(product=product, user=user, quantity=quantity)

    return redirect(to=reverse('shop:shopping_cart'))


def remove_product(request, product_id):
    """ 删除购物车中的商品 """
    user = models.User.objects.get(name=request.session.get('username'))
    product = models.Product.objects.get(pk=product_id)
    user.cart_set.filter(product=product).filter().first().delete()
    return redirect(to=reverse('shop:shopping_cart'))


def category(request, category_id):
    """ 分类展示商品 """
    category_ = models.Category.objects.get(pk=category_id)
    products = category_.product_set.all()
    return render_shop(request, products)


def tag(request, tag_id):
    """ 由标签展示商品 """
    tag_ = models.Tag.objects.get(pk=tag_id)
    products = tag_.product_set.all()
    return render_shop(request, products)


def price_filter(request):
    """ 由价格过滤商品 """
    minvalue = request.POST.get('minvalue')
    maxvalue = request.POST.get('maxvalue')
    products = models.Product.objects.filter(price__gte=minvalue, price__lte=maxvalue)
    print(products, maxvalue, minvalue)
    return render_shop(request, products)


def review(request, product_id):
    username = request.session.get('username')
    user = models.User.objects.get(name=username)
    product = models.Product.objects.get(pk=product_id)
    # 计算商品小星星
    stars = int(request.POST.get('stars'))
    score = product.star * product.review_set.count()
    product.star = (score + stars) / (product.review_set.count() + 1)

    content = request.POST.get('content')
    models.Review.objects.create(content=content, user=user, product=product, stars=stars)
    return redirect(to=reverse('shop:shop_single', args=product_id))


def search(request):
    product_name = request.POST.get('product_name')
    products = models.Product.objects.filter(name__contains=product_name)
    return render_shop(request, products)

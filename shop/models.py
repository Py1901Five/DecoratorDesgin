from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    pwd = models.CharField(max_length=20)
    image = models.ImageField(upload_to='users', default='users/author-thumb-2.jpg')

    def __str__(self):
        return self.name


class Product(models.Model):
    """ 商品 """
    name = models.CharField(max_length=50)
    star = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], default=5)
    price = models.FloatField()
    image = models.ImageField(upload_to='products')
    remains = models.IntegerField(default=100)
    describe = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(to='Category', on_delete=None)
    tag = models.ForeignKey(to='Tag', on_delete=None)

    def __str__(self):
        return self.name


class Cart(models.Model):
    """ 购物车 """
    user = models.ForeignKey(to='User', on_delete=None)
    product = models.ForeignKey(to='Product', on_delete=None)
    quantity = models.PositiveIntegerField(default=1)


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField()
    stars = models.FloatField()
    user = models.ForeignKey(to='User', on_delete=None)
    product = models.ForeignKey(to='Product', on_delete=None)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content


from django.db import models

# Create your models here.


class Service(models.Model):
    title = models.CharField(max_length=30)
    message = models.TextField()
    span = models.CharField(max_length=100,null=True,blank=True)


class Trait(models.Model):
    span = models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    message = models.TextField()


class Stylist(models.Model):
    message = models.TextField()
    image = models.TextField()
    name = models.CharField(max_length=50)


class ShopList(models.Model):
    image = models.TextField()
    title = models.CharField(max_length=80)
    price = models.CharField(max_length=50)
    new_price = models.CharField(max_length=50)


class Pricing(models.Model):
    '''价格定价页'''
    title = models.CharField(max_length=50)
    pricing = models.IntegerField()
    text1 = models.TextField()
    text2 = models.TextField()
    text3 = models.TextField()
    text4 = models.TextField()


class Question(models.Model):
    '''疑问解惑也的问题'''
    question = models.TextField()
    message = models.TextField()

class Potential(models.Model):
    '''潜在用户表，客户提交问题'''
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    question = models.TextField()

class Team(models.Model):
    '''公司团队'''
    name= models.CharField(max_length=50)
    message = models.TextField()
    image = models.TextField()
    profession = models.CharField(max_length=50)
    addr = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    '''团队成员教育史'''
    school = models.CharField(max_length=100)
    time = models.TextField()
    message = models.TextField()
    teamid = models.ForeignKey(Team,on_delete=models.CASCADE)



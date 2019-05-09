from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Type(models.Model):
    """文章分类"""
    tName = models.CharField(max_length=20, default='纹理会话')

    def __str__(self):
        return self.tName


class Tag(models.Model):
    """文章标签"""
    tName = models.CharField(max_length=20, default='家具')

    def __str__(self):
        return self.tName


class UserSell(models.Model):
    """用户类"""
    # todo 添加图片继承form
    uheaderImg = models.ImageField(upload_to='userHeaders')
    uName = models.CharField(max_length=20, default='bh')
    uPwd = models.CharField(max_length=10, default='000')
    uType = models.CharField(max_length=10, default='sell')
    # 简介
    uBrief = models.CharField(max_length=50)


class Article(models.Model):
    """文章"""
    aAuthor = models.ForeignKey(UserSell, on_delete=models.CASCADE)
    aTitle = models.CharField(max_length=20)
    aPublicTime = models.DateTimeField(auto_now=True)
    aContent = HTMLField()
    aType = models.ForeignKey(Type, on_delete=models.CASCADE)
    # 多对多
    aTag = models.ManyToManyField(Tag)
    aBackgroundImage = models.ImageField(upload_to='articleImages')
    aReadNum = models.SmallIntegerField(default='0')


class Comment(models.Model):
    """评论"""
    cPublicPeople = models.CharField(max_length=20)
    cEmail = models.EmailField()
    cPhone = models.CharField(max_length=11)
    cUrl = models.URLField()
    cContent = models.CharField(max_length=500)
    cArticle = models.ForeignKey(Article, on_delete=models.CASCADE)
    # cComtent = models.ForeignKey('self', on_delete=models.CASCADE)




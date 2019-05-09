from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class UserInfo(models.Model):
    subject = models.CharField(max_length=26,null=True,blank=True)
    name = models.CharField(max_length=16)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=13,null=True)
    message = models.TextField(max_length=660,null=True)

    def __str__(self):
        return self.name


class Classify(models.Model):
    classify = models.CharField(max_length=16)

    def __str__(self):
        return self.classify


class Furniture(models.Model):
    imgname = models.CharField(max_length=16)
    indexn = models.SmallIntegerField()
    img = models.ImageField(upload_to='hotpic')
    classifies = models.ManyToManyField(Classify)

    def __str__(self):
        return self.imgname


class FurnitureInfo(models.Model):
    tag = models.CharField(max_length=90)
    pub_date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=26)
    tagweb = models.URLField(max_length=36)
    tofu = models.ForeignKey(Furniture, models.CASCADE)
    title = models.CharField(max_length=150)
    descirbe = HTMLField()

    def __str__(self):
        return self.title


class Furnitureimg(models.Model):
    name = models.CharField(max_length=16)
    furimg = models.ImageField(upload_to='hotpic')
    index = models.SmallIntegerField()
    fore = models.ForeignKey(Furniture, models.CASCADE)

    def __str__(self):
        return self.name


class FullWidth(models.Model):
    name = models.CharField(max_length=16)
    fullpic = models.ImageField(upload_to='fullwidth')
    fyr = models.ForeignKey(Classify, models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name


class TextPic(models.Model):
    tag = models.CharField(max_length=16)
    deti = models.CharField(max_length=16)
    img = models.ImageField(upload_to='textimg')
    fyr = models.ForeignKey(Classify, models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.tag


class SingTwo(models.Model):
    singimg = models.ImageField(upload_to='singtwo')
    name = models.CharField(max_length=16)
    sfor = models.ForeignKey(FullWidth, models.CASCADE, null=True, blank=True)
    timgfy = models.ForeignKey(TextPic, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

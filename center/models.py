import datetime
from django.db import models
from django.utils import timezone

##
## 部门表
##
class Department(models.Model):
    title   = models.CharField(max_length=255, unique=true, verbose_name=u"部门名称")
    weigths = models.FloatField(verbose_name=u"权重")
    token   = models.CharField(max_length=32, verbose_name=u"")

##
## 个人表
##
class Person(models.Model):
    name      = models.CharField(max_length=255, verbose_name=u"姓名")
    sex       = models.SmallIntegerField(max_length=1, default=1, verbose_name=u"性别1男2女")
    id_number = models.CharField(max_length=18, null=False, verbose_name=u"身份证号")
    address   = models.CharField(max_length=255, null=True, verbose_name=u"地址")
    token     = models.CharField(max_length=32, null=False, unique=True, verbose_name=u"token", primary_key=True)


##
## 个人元信息表
##
class PersonInfo(models.Model):
    department  = models.ForeignKey(Department, on_delete=models.CASCADE)
    verify      = models.BooleanField(default=False, verbose_name=u"是否已经审核")
    title       = models.CharField(max_length=255, unique=True, verbose_name=u"标题")
    description = models.CharField(max_length=255, verbose_name=u"描述")
    remark      = models.CharField(max_length=255, verbose_name=u"备注")
    score       = models.FloatField(verbose_name=u"分数")
    maximum_score = models.FloatField(verbose_name=u"此项可获取的最高分数")


##
## 分数表
##
class Score(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    score  = models.FloatField(verbose_name="分数")
    year   = models.SmallIntegerField(max_length=4, verbose_name=u"年份")
    month  = models.SmallIntegerField(max_length=2, verbose_name=u"月份")
    day    = models.SmallIntegerField(max_length=2, verbose_name=u"天数")
    time   = models.IntegerField(max_length=15, verbose_name=u"unix时间戳")

from django.db import models

# 定义项目表


class Project(models.Model):
    NUM_Project = models.CharField(verbose_name='项目编号', max_length=100)
    NAME_Project = models.CharField(verbose_name='项目名称', max_length=100)
    TYPE_Project = models.CharField(verbose_name='项目类型', max_length=100)
    VALUE_Project = models.IntegerField(verbose_name='项目价值', default=0)
    START_Project = models.DateField(verbose_name='项目开始时间')
    END_Project = models.DateField(verbose_name='项目结束时间')
    ADDRESS_Project = models.CharField(verbose_name='项目地址', max_length=100)
    DESC_Project = models.CharField(verbose_name='项目描述', max_length=1000)
    id = models.AutoField(primary_key=True)


# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    """
    Blog class
    """
    STATUS_IN_BLOG_CHOICES = (
        ('AUTO', '系统自动保存'),
        ('SAVE', '保存'),
    )
    title = models.CharField('标题', max_length = 200, blank = True)
    content = models.TextField('正文', blank = True)
    user = models.ForeignKey(User, verbose_name = '作者')
    status = models.CharField('状态', max_length = 10, choices = STATUS_IN_BLOG_CHOICES, default = 'SAVE')
    mart_public = models.NullBooleanField('发布', default = False)
    mark_delete = models.NullBooleanField('删除', default = False)
    modify_time = models.DateTimeField('修改时间', auto_now = True)
    create_time = models.DateTimeField('创建时间', auto_now_add = True)
    
    class Meta:
        verbose_name_plural = '博客'
        ordering = ['-modify_time', '-create_time']
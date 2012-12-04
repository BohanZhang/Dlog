# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import logging
from models import Blog

logger = logging.getLogger(__name__)

def get_blog(request, id):
    """
        取得Blog
    """
    template = 'blog/blog.html'
    parameters = {}
    parameters['mark_public'] = True
    parameters['id'] = id
    
    logger.info('Get blog, id: %s' % id)
    blog = Blog.objects.get(**parameters)
    logger.debug('blog get: %s' % blog)
    
    data = {}
    data['blog'] = blog
    return render_to_response(template, data)

def get_blog_list(request):
    """
        取得博客列表
    """
    template = 'blog/blog_list.html'
    
    parameters = {}
    parameters['mark_public'] = True
    
    blog_list = Blog.objects.filter(**parameters)
    
    data = {}
    data['blog_list'] = blog_list
    return render_to_response(template, data)
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import logging
from models import Blog

logger = logging.getLogger(__name__)

def get_blog(request, id):
    """
        Get one blog.
    """
    template = 'blog/blog.html'
    parameters = {}
    parameters['mark_public'] = True
    parameters['id'] = id
    
    logger.info('Get blog, id: %s' % id)
    blog = get_object_or_404(Blog, **parameters)
    logger.debug('blog get: %s' % blog)
    
    data = {}
    data['blog'] = blog
    return render_to_response(template, data)

def get_blog_list(request):
    """
        Get blog list.
    """
    template = 'blog/blog_list.html'
    
    parameters = {}
    parameters['mark_public'] = True
    
    blog_list = Blog.objects.filter(**parameters)
    
    data = {}
    data['blog_list'] = blog_list
    return render_to_response(template, data)

def save_blog(request):
    """
    Ajax save the blog.
    """
    json_data = request.body
    logger.debug(json_data)

def edit_blog(request):
    template = 'blog/blog_edit.html'
    
    blog = get_object_or_404(Blog, pk = 2)
    
    data = {}
    data['blog'] = blog
    return render_to_response(template, data, context_instance = RequestContext(request))
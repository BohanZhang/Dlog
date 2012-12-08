from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'(?P<id>\d+)/', 'get_blog'),
    url(r'list/', 'get_blog_list'),
    url(r'edit/', 'edit_blog'),
)

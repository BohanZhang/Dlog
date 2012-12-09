from django.contrib import admin
from models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'mark_public', 'status')
    fields = ('title', 'content', 'mark_public')

admin.site.register(Blog, BlogAdmin)
#coding:utf-8
from django import forms
from django.contrib.markup.templatetags.markup import restructuredtext
from django.core import urlresolvers
from DjangoUeditor.widgets import UEditorWidget
import xadmin
from .models import Post
from .models import Category
from .models import Page
from .models import Widget
from .models import STYLE 
from .models import SiteInfo
from django.db import models
#TODO: 兼容markdown和reStructuredText

class PostAdmin(object):
    #form = PostAdminForm
    search_fields = ('title', 'alias')
    fields = ('title', 'content',  'summary', 'alias', 'tags', 'status',
              'category', 'is_top', 'style', 'pub_time')
    style_fields = {"content": 'ueditor'}

    def get_field_style(self, db_field, style, **kwargs):
        if style in ('ueditor',):
            ue = UEditorWidget(width=800,height=500, imageManagerPath="post/", imagePath='post/', filePath='post/', toolbars='full')
            attrs = {'widget': ue} 
            return attrs
    
    list_display = ('preview', 'title', 'category', 'is_top', 'pub_time')
    ordering = ('-pub_time', )
    save_on_top = True


    def preview(self, obj):
        url_edit = urlresolvers.reverse('xadmin:blog_post_change', args=(obj.id,))
        return u'''
                    <span><a href="/%s.html" target="_blank">预览</a></span>
                    <span><a href="%s" target="_blank">编辑</a></span>
                ''' % (obj.alias, url_edit)

    preview.short_description = u'操作'
    preview.allow_tags = True

    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        #if not obj.summary:
        #    obj.summary = obj.content
        if STYLE[obj.style] == u'html':
            obj.content_html = obj.content
        else:
            obj.content_html = obj.content
        obj.save()


class CategoryAdmin(object):
    search_fields = ('name', 'alias')
    list_display = ('name', 'rank', 'is_nav', 'status', 'create_time')

class PageAdmin(object):
    search_fields = ('name', 'alias')
    fields = ('title', 'alias', 'link', 'content', 'style', 'status', 'rank')
    list_display = ('title', 'link', 'rank', 'status', 'style')
    style_fields = {"content": 'ueditor'}

    def get_field_style(self, db_field, style, **kwargs):
        if style in ('ueditor',):
            ue = UEditorWidget(width=800,height=500, imageManagerPath="post/", imagePath='post/', filePath='post/', toolbars='normal')
            attrs = {'widget': ue} 
            return attrs
    
    def save_models(self):
        obj = self.new_obj
        obj.author = self.request.user
        
        if STYLE[obj.style] == u'html':
            obj.content_html = obj.content
        else:
            obj.content_html = obj.content

        '''
        if obj.is_html:
            obj.content_html = obj.content
        else:
            obj.content_html = restructuredtext(obj.content)
        '''
        obj.save()


class WidgetAdmin(object):
    search_fields = ('name', 'alias')
    fields = ('title', 'content', 'rank', 'hide')
    list_display = ('title', 'rank', 'hide')


xadmin.site.register(Post, PostAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Page, PageAdmin)
xadmin.site.register(Widget, WidgetAdmin)
xadmin.site.register(SiteInfo)

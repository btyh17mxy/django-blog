#coding:utf-8
from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps import views as sitemap_views
from django.views.decorators.cache import cache_page

#from django.contrib import admin
#admin.autodiscover()
import xadmin
xadmin.autodiscover()

from blog.views import (IndexView, CategoryListView, TagsListView,
                        PostDetailView, PageDetailView)
from feeds import LatestEntriesFeed
from sitemap import PostSitemap
import debug_toolbar
import settings

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^feed|rss/$', LatestEntriesFeed()),
    #url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^sitemap\.xml$', cache_page(sitemap_views.sitemap, 60 * 60 * 12), {'sitemaps': {'posts': PostSitemap}}),
    url(r'^category/(?P<alias>\w+)/', CategoryListView.as_view()),
    url(r'^tag/(?P<tag>[\w|\.|\-]+)/$', TagsListView.as_view()),
    url(r'xadmin/', include(xadmin.site.urls), name='xadmin'),
    #url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc', name='xmlrpc'),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    #放到最后
    url(r'^(?P<slug>[\w|\-|\d|\W]+?).html$', PostDetailView.as_view()),
    url(r'^(?P<slug>\w+)/$', PageDetailView.as_view()),
)

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )

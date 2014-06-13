#coding:utf-8

from django.contrib.sitemaps import Sitemap

from blog.models import Post

class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.2

    print '&'*90
    def items(self):
        return Post.objects.filter(status=0)

    def lastmod(self, obj):
        return obj.update_time

    def location(self, obj):
        return '/%s.html' % obj.alias

from django.contrib.sitemaps import Sitemap
from .models import Post
from django.shortcuts import reverse


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_pub

    #def location(self, obj):
     #   return obj.slug


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['posts_list_url', 'faq_url', 'contacts_url']

    def location(self, item):
        return reverse(item)


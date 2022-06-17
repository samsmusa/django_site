from django.contrib.sitemaps import Sitemap
from .models import Blog, Scholarships, Internship
 
 
class ScholarshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Scholarships.objects.all()

    def lastmod(self, obj):
        return obj.add_date


class InternshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Internship.objects.all()

    def lastmod(self, obj):
        return obj.add_date

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = 'https'

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.add_date
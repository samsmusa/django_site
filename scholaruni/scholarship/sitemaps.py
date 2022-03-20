from django.contrib.sitemaps import Sitemap
from .models import Scholarships, Internship
 
 
class ScholarshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Scholarships.objects.all()

    def lastmod(self, obj):
        return obj.add_date


class InternshipSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Internship.objects.all()

    def lastmod(self, obj):
        return obj.add_date
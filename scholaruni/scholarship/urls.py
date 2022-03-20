from django.urls import path
from .views import ScholarshipDetailView, ScholarshipView,InternshipView,search, about, about, createMessage,HomeView, InternshipDetailView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ScholarshipSitemap,InternshipSitemap

sitemaps = {
    'scholarship':ScholarshipSitemap,
    'internship':InternshipSitemap
}


urlpatterns = [
    path('', HomeView, name="home"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # path('', ScholarshipListView.as_view(), name="scholarships"),
    path('search/', search, name="search"),
    path('scholarships/', ScholarshipView, name="scholarships"),
    path('internships/', InternshipView, name="internships"),
    path('scholarship/<slug:slug>', ScholarshipDetailView, name="scholar_blog"),
    path('internship/<slug:slug>', InternshipDetailView, name="intern_blog"),
    path('contact/', createMessage, name="contact"),
    path('about/', about, name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
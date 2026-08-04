# sitemaps.py
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone

from portfolio.models import campaign_funnel, campaign_faq, campaign_blog, portfolio_projects


class StaticViewSitemap(Sitemap):
    changefreq = "annually"
    priority = 0.4
    protocol = 'https'

    def items(self):
        return ['contact_us_html', 'about_us_html', 'privacy_html', 'terms_html', 'home_page_html', 'llms_html'] 

    def location(self, item):
        return reverse(item)

class FunnelSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return campaign_funnel.objects.exclude(slug__isnull=True).exclude(slug="").order_by('id')

    def lastmod(self, obj):
        return timezone.now()

class ServicesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return portfolio_projects.objects.exclude(slug__isnull=True).exclude(slug="").order_by('id')

    def lastmod(self, obj):
        return timezone.now()

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return campaign_blog.objects.exclude(slug__isnull=True).exclude(slug="").order_by('id')

    def lastmod(self, obj):
        return timezone.now()

class FAQSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return campaign_faq.objects.exclude(slug__isnull=True).exclude(slug="").order_by('id')

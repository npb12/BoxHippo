from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from listings.views import listings, edit_listing

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boxhippo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', listings),
    url(r'^edit/(?P<listingID>\d|N)/$', edit_listing),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

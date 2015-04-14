from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from listings.views import listings, edit_listing, view_listing, upload_picture, remove_picture

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boxhippo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', listings),
    url(r'^view/(?P<lid>\d*|N)/$', view_listing),
    url(r'^edit/(?P<listingID>\d*|N)/$', edit_listing),
    url(r'^upload-pic/(?P<listingID>\d*)/$', upload_picture),
    url(r'^remove-pic/(?P<listingID>\d*)/$', remove_picture),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

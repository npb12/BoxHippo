from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from users.views import register

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boxhippo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^register/', CreateView.as_view(template_name="registration/register.html", form_class=UserCreationForm, success_url="/listings/")),
    url(r'^register/', register),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', 'listings.views.listings'),
    url(r'^listings/', include('listings.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^merchants/$', TemplateView.as_view(template_name="basics/landing.html")),
    url(r'base/$', TemplateView.as_view(template_name="basics/base.html")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^ajax_select/', include('ajax_select.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^django_messages/', include('django_messages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'logout$',logout,{'next_page':'/'},),
    url(r'^$','auth.views.index'),
    url(r'^inbox/$', 'django_messages.views.inbox'),
)
if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

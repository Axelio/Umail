from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^ajax_select/', include('ajax_select.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^django_messages/', include('django_messages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^ajax_select/', include('ajax_select.urls')),
    (r'^admin/lookups/', include(ajax_select_urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^django_messages/', include('django_messages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'logout$',logout,{'next_page':'/'},),
    url(r'^$','auth.views.index'),
    url(r'^entrada/$', 'django_messages.views.inbox', name='messages_inbox'),
    url(r'^enviados/$', 'django_messages.views.outbox', name='messages_outbox'),
    url(r'^por_aprobar/$', 'django_messages.views.por_aprobar', name='por_aprobar'),
    url(r'^por_aprobar/(?P<message_id>[\d]+)/$', 'django_messages.views.ver_por_aprobar', name='ver_por_aprobar'),
    url(r'^aprobar/(?P<message_id>[\d]+)/$', 'django_messages.views.aprobar', name='aprobar'),
    url(r'^anular/(?P<message_id>[\d]+)/$', 'django_messages.views.anular', name='anular'),
    url(r'^redactar/$', 'django_messages.views.compose'),
    url(r'^responder/(?P<message_id>[\d]+)/$', 'django_messages.views.reply', name='messages_reply'),
    url(r'^eliminar/(?P<message_id>[\d]+)/$', 'django_messages.views.delete', name='messages_delete'),
    url(r'^papelera/$', 'django_messages.views.trash', name='messages_trash'),
    url(r'^leer/(?P<message_id>[\d]+)/$', 'django_messages.views.view', name='messages_detail'),
)

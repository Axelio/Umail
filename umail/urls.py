from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from django.views.generic import TemplateView
from auth.views import *
from django.contrib.auth.decorators import login_required
from django_select.views import AutoResponseView

admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^noticias/', include('noticias.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'logout$',logout,{'next_page':'/'}, name='salir'),
    url(r'^$','auth.views.index', name='inicio'),
    url(r'^lookup/.*$', 'django_messages.views.destinatarios_lookup'),
    url(r'^fields/auto.json$', AutoResponseView.as_view(), 'django_select2_central_json'),

   (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    # Auth
    url(r'^auth$', Auth.as_view(), name='auth'),
    url(r'^preguntas_secretas/$', Revisar_preguntas.as_view(), name='preguntas_secretas'),

    # Manual de usuario 
    url(r'^ayuda/(?P<seccion>\w+)/$', 'manual_usuario.views.manual', name='manual_usuario'),

    url(r'^ayuda/$', 'manual_usuario.views.manual', name='manual_usuario'),

    # Memos
    ## Bandejas
    url(r'^bandeja/(?P<tipo_bandeja>\w+)/$', 'django_messages.views.bandeja', name='bandeja'),

    ## Entrada
    url(r'^entrada/$', 'django_messages.views.bandeja', name='messages_inbox'),

    ## Enviados
    url(r'^enviados/$', 'django_messages.views.outbox', name='messages_outbox'),

    ## Memos por aprobar
    url(r'^por_aprobar/$', 'django_messages.views.por_aprobar', name='por_aprobar'),
    url(r'^por_aprobar/(?P<message_id>[\d]+)/$', 'django_messages.views.ver_por_aprobar', name='ver_por_aprobar'),

    ## Memo para aprobar
    url(r'^aprobar/(?P<message_id>[\d]+)/$', 'django_messages.views.aprobar', name='aprobar'),

    ## Memo para anular
    url(r'^anular/(?P<message_id>[\d]+)/$', 'django_messages.views.anular', name='anular'),

    ## Redactar memo
    url(r'^redactar/$', 'django_messages.views.compose', name='redactar'),
    ## Responder memo
    url(r'^responder/(?P<message_id>[\d]+)/$', 'django_messages.views.reply', name='messages_reply'),
    ## Archivar memo
    url(r'^archivar/(?P<message_id>[\d]+)/$', 'django_messages.views.delete', name='messages_delete'),

    ## Memos archivados
    url(r'^archivados/$', 'django_messages.views.trash', name='messages_trash'),

    ## Leer memo
    url(r'^leer/(?P<message_id>[\d]+)/$', 'django_messages.views.view', name='messages_detail'),


    # Personas
    ## Perfil
    url(r'^perfil/', include('personas.urls')),

    url(r'^contactos/', 'personas.views.contactos'),

    # Reportes
    ## Perfil
    url(r'^reportes/$', 'reportes.views.index', name='reportes'),
    url(r'^descargas/memo/(?P<message_id>[\d]+)/$', 'reportes.views.memo'),
)

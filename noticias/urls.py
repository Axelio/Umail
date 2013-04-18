# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.auth.views import logout, login
urlpatterns=patterns('',
    (r'^(\d+)$','noticias.views.detalle_noticia'),
    (r'^.*$', 'noticias.views.todas_noticias'), #Vista por defecto
)

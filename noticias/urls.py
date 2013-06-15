# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns=patterns('',
    (r'^(\d+)$','noticias.views.detalle_noticia'),
    (r'^.*$', 'noticias.views.todas_noticias'), #Vista por defecto
)

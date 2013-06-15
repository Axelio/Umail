# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns=patterns('',
    (r'^.*$', 'personas.views.perfil'), #Vista por defecto
)

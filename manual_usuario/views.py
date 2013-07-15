# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from manual_usuario.models import *

def manual(request, seccion=None):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    manuales = ''
    if seccion == None:
        titulo = u'¿Cómo podemos ayudarte?'
    else:

        # Si es general, se filtran TODAS las noticias
        if seccion == 'general':
            manuales = Manual.objects.all()
        elif seccion == 'primeros_pasos':
            manuales = Manual.objects.filter(seccion__iexact='Perfiles')
        else:
            manuales = Manual.objects.filter(seccion__iexact=seccion)
        if manuales.exists():
            if seccion == 'general':
                titulo = "Toda la ayuda disponible"
            elif seccion == 'primeros_pasos':
                titulo = "Tus primeros pasos..."
            else:
                titulo = u'Todo acerca de los %s' %(seccion)
        else:
            titulo = u'No se encontró ningún manual sobre %s' %(seccion)
    diccionario.update({'manuales':manuales})

    diccionario.update({'titulo':titulo})
    return render_to_response('user/manual_usuario/manuales.html', diccionario)

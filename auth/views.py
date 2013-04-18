# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

def index(request):
    diccionario = {}
    diccionario.update(csrf(request))
    loggeado = request.user.is_authenticated()
    diccionario.update({'loggeado':loggeado})
    if loggeado:
        ultimas_noticias = Noticias.objects.all().order_by('-fecha')[:2]
        diccionario.update({'ult_notic':ultimas_noticias})

    return render_to_response('user/index.html', diccionario)

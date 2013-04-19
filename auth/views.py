# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from auth.forms import AuthenticacionForm
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    mensaje = '' 

    if request.method == 'POST':
        user = User.objects.filter(Q(username=request.POST['username'])|Q(email=request.POST['username']))
        if user.exists():
            request.user = user[0]
        else:
            mensaje = "Usuario no existente"
    loggeado = request.user.is_authenticated()
    diccionario.update({'loggeado':loggeado})

    diccionario.update({'mensaje':mensaje})

    if loggeado:
        ultimas_noticias = Noticias.objects.all().order_by('-fecha')[:2]
        diccionario.update({'ult_notic':ultimas_noticias})
        return login(request,template_name='user/index/index.html', extra_context=diccionario) #extra_context={'mensaje':'mssdensaje'
    else:
        return login(request,template_name='user/index/index.html', authentication_form=AuthenticacionForm, extra_context=diccionario) #extra_context={'mensaje':'mssdensaje'

    #return render_to_response('user/index/index.html', diccionario)

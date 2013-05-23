# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect

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
        ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:7]
        ultimas_noticias2 = Noticias.objects.all().order_by('-fecha')[8:]
        diccionario.update({'ult_notic1':ultimas_noticias1})
        diccionario.update({'ult_notic2':ultimas_noticias2})
        return login(request,template_name='user/index/index.html', extra_context=diccionario) #extra_context={'mensaje':'mssdensaje'
    else:
        return render_to_response('user/index/index.html', diccionario)

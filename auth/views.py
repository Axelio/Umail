# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from auth.forms import AuthenticacionForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect

def auth(request):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    if request.user.is_authenticated():
        return index(request)

    diccionario.update({'form':AuthenticacionForm()})

    if request.method == 'POST':
        import pdb
        diccionario.update({'form':AuthenticacionForm(request.POST)})
        usuario = User.objects.filter(Q(username=request.POST['username'])|Q(email=request.POST['username']))
        if usuario.exists(): 
            usuario = usuario[0]
            user = authenticate(username=usuario, password=request.POST['password'])

            if user is not None:
                login(request, usuario)
                #"User is not valid, active and authenticated"
                if not user.is_active:
                    mensaje = "La contraseña es válida pero la cuenta ha sido desactivada."
                    diccionario.update({'m_error':mensaje})
                    return render_to_response('usuario/index/login.html', diccionario)
                return index(request) 
            else:
                # El usuario o contraseña eran incorrectos
                mensaje = "Contraseña incorrecta. Por favor, inténtelo nuevamente."
                diccionario.update({'m_error':mensaje})

        else:
            # El usuario no existe
            mensaje = "El usuario %s no existe." %(request.POST['username'])
            diccionario.update({'m_error':mensaje})
        return render_to_response('usuario/index/login.html', diccionario)

    else:
        return render_to_response('usuario/index/login.html', diccionario)

def index(request):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:3]
    ultimas_noticias2 = Noticias.objects.all().order_by('-fecha')[3:6]
    diccionario.update({'ult_notic1':ultimas_noticias1})
    diccionario.update({'ult_notic2':ultimas_noticias2})
    mensaje = '' 
    loggeado = False

    return render_to_response('usuario/index/index.html', diccionario)

# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect

def index(request):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    diccionario.update({'form':AuthenticationForm()})
    ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:2]
    ultimas_noticias2 = Noticias.objects.all().order_by('-fecha')[3:5]
    diccionario.update({'ult_notic1':ultimas_noticias1})
    diccionario.update({'ult_notic2':ultimas_noticias2})
    mensaje = '' 
    loggeado = False

    if request.method == 'POST':
        diccionario.update({'form':AuthenticationForm(request.POST)})
        usuario = User.objects.filter(Q(username=request.POST['username'])|Q(email=request.POST['username']))
        if usuario.exists(): 
            usuario = usuario[0]
            user = authenticate(username=usuario, password=request.POST['password'])

            if user is not None:
                login(request, usuario)
                #"User is not valid, active and authenticated"
                if not user.is_active:
                    mensaje = "La contraseña es válida pero la cuenta ha sido desactivada"
                    diccionario.update({'m_error':mensaje})
                return render_to_response('user/index/index.html', diccionario)
        else:
            # El usuario o contraseña eran incorrectos
            mensaje = "El usuario y/o la contraseña son incorrectos"
            diccionario.update({'m_error':mensaje})
        return render_to_response('user/index/index.html', diccionario)

    else:
        return render_to_response('user/index/index.html', diccionario)

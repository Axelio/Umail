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
from reportes.forms import Feedback_Form
from reportes.models import Comentarios

def auth(request):
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    diccionario.update({'form':AuthenticationForm()})
    ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:3]
    diccionario.update({'ult_notic1':ultimas_noticias1})
    mensaje = '' 
    loggeado = False

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
    feedback_form, procesado = revisar_comentario(request)
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    diccionario.update({'feedback_form':feedback_form})
    ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:3]
    diccionario.update({'ult_notic1':ultimas_noticias1})
    mensaje = '' 
    loggeado = False

    return render_to_response('usuario/index/index.html', diccionario)

def revisar_comentario(request):
    procesado = False
    if request.method == 'POST':
        form = Feedback_Form(request)
        sentimiento = request.POST['sentimiento']
        pregunta = request.POST['pregunta']
        comentario = request.POST['comentario']
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        comentario = Comentarios.objects.create(
                                                sentimiento = sentimiento,
                                                pregunta = pregunta,
                                                comentario = comentario,
                                                nombre = nombre,
                                                correo = correo
            )
        procesado = True

    feedback_form = Feedback_Form()
    return feedback_form, procesado
# -*- coding: utf-8 -*-
from noticias.models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response, render
from auth.forms import AuthenticacionForm, PreguntasForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from reportes.forms import Feedback_Form
from reportes.models import Comentarios
from lib.umail import msj_expresion, renderizar_plantilla
from django.template import RequestContext
from django.views.generic.base import View
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from auth.models import PreguntasSecretas, Pregunta

class Auth(View):
    tipo_mensaje = ''
    expresion = ''
    mensaje = ''
    form = AuthenticacionForm
    noticias = Noticias.objects.all().order_by('-fecha')[:3] # Últimas 3 noticias
    template = 'usuario/auth/login.html'
    diccionario = {}
    diccionario.update({'noticias':noticias})
    
    def get(self, request, *args, **kwargs):
        self.form = self.form()
        if request.user.is_authenticated():
            if request.GET.has_keys['next']:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect('/')
            
        return renderizar_plantilla(request, 
                            plantilla = self.template, 
                            tipo_mensaje = self.tipo_mensaje, 
                            expresion = self.expresion, 
                            mensaje = self.mensaje, 
                            form = self.form
                        )

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        self.diccionario.update({'form':self.form})
        usuario = User.objects.filter(Q(username=request.POST['username'])|Q(email=request.POST['username']))
        self.diccionario.update({'request':request})
        if usuario.exists(): 
            usuario = usuario[0]
            user = authenticate(username=usuario, password=request.POST['password'])

            if user is not None:
                login(request, usuario)
                #"User is not valid, active and authenticated"
                if not user.is_active:
                    self.mensaje = u"La contraseña es válida pero la cuenta ha sido desactivada."
                    (self.tipo_mensaje, self.expresion) = msj_expresion('error')
                    return renderizar_plantilla(request, 
                                        plantilla = self.template, 
                                        tipo_mensaje = self.tipo_mensaje, 
                                        expresion = self.expresion, 
                                        mensaje = self.mensaje, 
                                        form = form
                                    )
                else:
                    # El usuario se loggea correctamente
                    return HttpResponseRedirect('/preguntas_secretas/')
            else:
                # El usuario o contraseña eran incorrectos
                self.mensaje = u"Contraseña incorrecta. Por favor, inténtelo nuevamente."
                (self.tipo_mensaje, self.expresion) = msj_expresion('error')
                return renderizar_plantilla(request, 
                                    plantilla = self.template, 
                                    tipo_mensaje = self.tipo_mensaje, 
                                    expresion = self.expresion, 
                                    mensaje = self.mensaje, 
                                    form = form
                                )
        else:
            # El usuario no existe
            self.mensaje = u"El usuario %s no existe." %(request.POST['username'])
            (self.tipo_mensaje, self.expresion) = msj_expresion('error')
            form = self.form(request.POST)
            return renderizar_plantilla(request, 
                                plantilla = self.template, 
                                tipo_mensaje = self.tipo_mensaje, 
                                expresion = self.expresion, 
                                mensaje = self.mensaje, 
                                form = form
                            )

from django.db import transaction

class Revisar_preguntas(View):
    from django.forms.formsets import formset_factory
    tipo_mensaje = ''
    expresion = ''
    mensaje = ''
    template = 'usuario/auth/preguntas.html'
    form = formset_factory(PreguntasForm, extra = 6)

    def get(self, request, *args, **kwargs):
        if not request.user.preguntassecretas_set.get_query_set().exists():
            form = self.form()
            self.mensaje = u'Para su mayor seguridad debe proporcionar algunas preguntas y respuestas secretas'
            (self.tipo_mensaje, self.expresion) = msj_expresion('alert')
            return renderizar_plantilla(request, 
                                plantilla = self.template, 
                                tipo_mensaje = self.tipo_mensaje, 
                                expresion = self.expresion, 
                                mensaje = self.mensaje, 
                                form = form 
                            )

        else:
            return HttpResponseRedirect('/')

    @transaction.commit_on_success
    def post(self, request, *args, **kwargs):
        
        form = self.form(request.POST)
        error = False

        if form.is_valid():
            posicion = 0
            usuario = request.user
            transaction.savepoint()

            for formulario in form.forms:
                pregunta = formulario['pregunta'].data
                pregunta = Pregunta.objects.get(id=pregunta)
                respuesta = formulario['respuesta'].data
                pregunta_secreta = PreguntasSecretas.objects.filter(usuario=usuario, pregunta=pregunta)
                if not pregunta_secreta.exists():
                    PreguntasSecretas.objects.create(usuario=usuario, pregunta=pregunta, respuesta=respuesta)
                else:
                    (self.tipo_mensaje, self.expresion) = msj_expresion('error')
                    self.mensaje = u'Al parecer la pregunta "%s" ya la has elegido más de una vez.' %(pregunta)
                    error=True

            if not error:
                transaction.commit()
                return HttpResponseRedirect('/')
            else:
                transaction.rollback()
                return renderizar_plantilla(request, 
                                    plantilla=self.template, 
                                    tipo_mensaje = self.tipo_mensaje, 
                                    expresion = self.expresion, 
                                    mensaje = self.mensaje, 
                                    form = form
                                )

            #transaction.commit()


def index(request):
    import datetime
    fecha_actual = datetime.datetime.today()
    diccionario = {}
    diccionario.update(csrf(request))
    diccionario.update({'request':request})
    diccionario.update({'fecha':fecha_actual})
    ultimas_noticias1 = Noticias.objects.all().order_by('-fecha')[:3]
    diccionario.update({'ult_notic1':ultimas_noticias1})
    mensaje = '' 
    loggeado = False

    return render_to_response('usuario/auth/index.html', diccionario)

def revisar_comentario(request):
    procesado = False
    if request.method == 'POST':
        form = Feedback_Form(request)
        pregunta = request.POST['pregunta']
        comentario = request.POST['comentario']
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        comentario = Comentarios.objects.create(
                                                pregunta = pregunta,
                                                comentario = comentario,
                                                nombre = nombre,
                                                correo = correo
            )
        procesado = True

    else:
        feedback_form = Feedback_Form()
        diccionario = {}
        diccionario.update(csrf(request))
        diccionario.update({'feedback_form':feedback_form})

        return render_to_response('usuario/feedback.html', diccionario)

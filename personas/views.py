# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from personas.forms import PerfilForm, FiltroForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django import forms
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models
from django.contrib.auth.forms import PasswordChangeForm
from auth.forms import PreguntasForm
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic.base import View
from django.forms.formsets import formset_factory
#from personas.forms import PreguntasForm
from django.forms.models import modelformset_factory
from django.forms import TextInput

from lib.umail import msj_expresion, renderizar_plantilla
from auth.models import PreguntasSecretas
import random

@csrf_protect
def contactos(request, template_name='user/contactos/index.html', mensaje=''):
    c = {}
    c.update(csrf(request))
    c.update({'request':request})
    from django_messages.models import Destinatarios
    from auth.models import Group
    lista_destinatarios = Destinatarios.objects.exclude(grupos__in=Group.objects.all())
    opcion = 'Listado de contactos'
    form = FiltroForm

    if request.method == "POST":
        form = FiltroForm(request.POST)
        if form.is_valid():
            q = request.POST['filtro']
            lista_destinatarios = lista_destinatarios.filter(models.Q(usuarios__user__userprofile__persona__primer_nombre__icontains=q)| # Primer nombre
                                                            models.Q(usuarios__user__userprofile__persona__primer_apellido__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__segundo_nombre__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__segundo_apellido__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__email__icontains=q)| # Correo
                                                            models.Q(usuarios__user__userprofile__persona__telefono__icontains=q)| # Telefono
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__cargo__name__icontains=q)| # Cargo
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__dependencia__departamento__icontains=q)| # Dependencia
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__dependencia__siglas__icontains=q) # Dependencia (siglas)

                                                            ).distinct()
            paginador = Paginator(lista_destinatarios, 20)
            pagina = request.GET.get('page')
            try:
                lista_destinatarios = paginador.page(pagina)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                lista_destinatarios = paginador.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                lista_destinatarios = paginador.page(paginador.num_pages)
            c.update({'form':form})
            c.update({'opcion':opcion})
            c.update({'lista_destinatarios':lista_destinatarios})
            print lista_destinatarios.object_list

            return render_to_response(template_name, c)
    paginador = Paginator(lista_destinatarios, 20)
    pagina = request.GET.get('page')
    try:
        lista_destinatarios = paginador.page(pagina)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lista_destinatarios = paginador.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lista_destinatarios = paginador.page(paginador.num_pages)
    c.update({'form':form})
    c.update({'opcion':opcion})
    c.update({'lista_destinatarios':lista_destinatarios})

    return render_to_response(template_name, c)
contactos = login_required(contactos)

@csrf_protect
def perfil(request, template_name='usuario/perfil/perfil.html', mensaje=''):
    c = {}
    c.update(csrf(request))
    c.update({'request':request})
  
    persona = PerfilForm(instance=request.user.profile.persona)
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            # Para editar los datos se le pasa el modelform  y se instancia con el request.profile.persona para guardar los cambios realizados
            form = PerfilForm(request.POST, instance=request.user.profile.persona)
            form.save()
            mensaje = 'Datos guardados exitosamente'
    c.update({
        'mensaje':mensaje,
        'persona':persona,
        })
    return render_to_response(template_name, c)
perfil = login_required(perfil)

@csrf_protect
def password_change(request,
                    template_name='user/personas/cambiar_clave.html',
                    post_change_redirect='user/personas/perfil.html',
                    password_change_form=PasswordChangeForm,
                    current_app=None, extra_context=None):
    if request.method == "POST":
        form = password_change_form(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            mensaje = u'Contraseña cambiada exitosamente'
            form = password_change_form(user=request.user)
            context.update({'form':form})
            context.update({'request':request})
            context.update({'mensaje':mensaje})
            return render_to_response(post_change_redirect, context)
    else:
        form = password_change_form(user=request.user)
        context = {
            'form': form,
            'request':request
        }
    return render_to_response(template_name, context)
password_change = login_required(password_change)

class PreguntasSecretas(View):
    from django.forms.formsets import formset_factory
    tipo_mensaje = ''
    expresion = ''
    mensaje = ''
    template = 'usuario/auth/preguntas.html'
    #form = PreguntasForm
    form = formset_factory(PreguntasForm, extra = 3)

    def get(self, request, *args, **kwargs):
        from auth.models import PreguntasSecretas
        if request.user.preguntassecretas_set.get_query_set().exists():
            form = self.form()
            preguntas = PreguntasSecretas.objects.filter(usuario=self.request.user)
            preguntas = random.sample(preguntas, 3)
            pregs = []
            for pregunta in preguntas:
                pre_id = pregunta.id
                pregs.append(pre_id)
            form = modelformset_factory(PreguntasSecretas, form = PreguntasForm, max_num=3, extra=0, )
            form = form(queryset=PreguntasSecretas.objects.filter(id__in=pregs))
            import pdb
            pdb.set_trace()
            form.form.base_fields['pregunta'].widget.attrs['disabled']=True
            #form.form.base_fields['respuesta'].widget.attrs['value']

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
            return HttpResponseRedirect('preguntas_secretas/')

    '''
    def post(self, request, *args, **kwargs):
        
        form = self.form(request.POST)
        error = False
    '''



class Cambiar_Clave(SessionWizardView):
    def get_template_names(self):
        if self.steps.current == '0':
            return 'usuario/perfil/preguntas_secretas.html'
        elif self.steps.current == '1':
            return 'usuario/perfil/cambiar_clave.html'

    def get_form(self, step=None, data=None, files=None):
        form = super(Cambiar_Clave, self).get_form(step, data, files)
        # determine the step if not given
        if step is None:
            step = self.steps.current

        # Paso 1: Preguntas secretas
        '''
        Se filtran las preguntas y respuestas personales del usuario.
        Se elijen aleatoriamente 3 preguntas.
        Se envían a la plantilla para que el usuario pueda responderlas
        '''
        if step == '0':
            preguntas = PreguntasSecretas.objects.filter(usuario=self.request.user)
            preguntas = random.sample(preguntas, 3)
            pregs = []
            for pregunta in preguntas:
                pre_id = pregunta.id
                pregs.append(pre_id)
            form = modelformset_factory(PreguntasSecretas, form = PreguntasForm, max_num=3, extra=0, )
            form = form(queryset=PreguntasSecretas.objects.filter(id__in=pregs))
        return form

    def done(self, form_list, **kwargs):
        Preguntas = form_list[0] # Formulario de preguntas secretas
        Cambiar_Clave = form_list[1] # Formulario de preguntas secretas
        if Preguntas.is_valid():
            if Cambiar_Clave.is_valid():
                print True
        return HttpResponseRedirect('/')


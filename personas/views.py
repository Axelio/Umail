# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from personas.forms import PerfilForm, FiltroForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import models

@csrf_protect
def contactos(request, template_name='user/contactos/index.html', mensaje=''):
    c = {}
    c.update(csrf(request))
    c.update({'request':request})
    from django_messages.models import Destinatarios
    from auth.models import Group
    lista_destinatarios = Destinatarios.objects.exclude(grupos__in=Group.objects.all())
    paginador = Paginator(lista_destinatarios, 2)
    page = request.GET.get('page')
    opcion = 'Listado de contactos'
    form = FiltroForm

    if request.method == "POST":
        form = FiltroForm(request.POST)
        if form.is_valid():
            q = request.POST['filtro']
            lista = lista_destinatarios.filter(models.Q(usuarios__user__userprofile__persona__primer_nombre__icontains=q)| # Primer nombre
                                                            models.Q(usuarios__user__userprofile__persona__primer_apellido__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__segundo_nombre__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__segundo_apellido__icontains=q)| # Primer apellido
                                                            models.Q(usuarios__user__userprofile__persona__email__icontains=q)| # Correo
                                                            models.Q(usuarios__user__userprofile__persona__telefono__icontains=q)| # Telefono
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__cargo__name__icontains=q)| # Cargo
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__dependencia__departamento__icontains=q)| # Dependencia
                                                            models.Q(usuarios__user__userprofile__persona__cargo_principal__dependencia__siglas__icontains=q) # Dependencia (siglas)

                                                            ).distinct()
            paginador = Paginator(lista, 2)
            try:
                lista = paginador.page(lista)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                lista = paginador.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                lista = paginador.page(paginator.num_pages)
            c.update({'form':form})
            c.update({'opcion':opcion})
            c.update({'lista_destinatarios':lista})

            return render_to_response(template_name, c)

    try:
        lista_destinatarios = paginador.page(lista_destinatarios)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        lista_destinatarios = paginador.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        lista_destinatarios = paginador.page(paginator.num_pages)
        
    c.update({'form':form})
    c.update({'opcion':opcion})
    c.update({'lista_destinatarios':lista_destinatarios})
    return render_to_response(template_name, c)
contactos = login_required(contactos)

@csrf_protect
def perfil(request, template_name='user/personas/perfil.html', mensaje=''):
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

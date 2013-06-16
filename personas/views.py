# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from personas.forms import PerfilForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.forms import PasswordChangeForm
from django.views.decorators.csrf import csrf_protect
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

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

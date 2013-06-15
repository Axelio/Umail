# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from personas.forms import PerfilForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def perfil(request, template_name='user/personas/perfil.html'):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
    else:
        form = PerfilForm()
    return render_to_response(template_name, {
        'form':form,
    }, context_instance=RequestContext(request))
    
perfil = login_required(perfil)



# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape
from django.utils.html import format_html

register = template.Library()
def menu(seccion):
    renderizar = ''

    titulos = []
    enlace = []
    clase = []
    vmenu=[]

    # Inicio
    titulos.append("Inicio")
    enlace.append("/")
    clase.append("nav1")

    # Memos
    titulos.append("Memos")
    enlace.append("/entrada/#Menu")
    clase.append("nav2")

    # Reportes
    titulos.append("Reportes")
    enlace.append("/noticias/#Menu")
    clase.append("nav4")

    # Perfil
    titulos.append("Perfil")
    enlace.append("/#Menu")
    clase.append("nav3")

    # Contactos
    titulos.append("Contactos")
    enlace.append("/#Menu")
    clase.append("nav5")

    vmenu.append(titulos)
    vmenu.append(enlace)

    activo = ''
    for posicion in range(titulos.__len__()):
        if titulos[posicion] == seccion:
            activo = 'id="active"'
        else:
            activo = ''
        url = '<li class='+ clase[posicion] +' '+ activo +'><a href='+ enlace[posicion] +'>'+ titulos[posicion] +'</a></li>'
        renderizar = renderizar + url


    return format_html(renderizar)
menu.is_safe = True 
register.filter(menu)

def num_entrada(request):
    from django_messages.models import Message, Destinatarios
    destinatario = Destinatarios.objects.get(usuarios__user=request.user)
    message_list = Message.objects.inbox_for(request.user).exclude(leido_por=destinatario).distinct()
    return message_list.count()
num_entrada.is_safe = True 
register.filter(num_entrada)

def jefe_departamento(request):
    if request.user.profile.persona.cargo_principal.cargo == request.user.profile.persona.cargo_principal.dependencia.cargo_max:
        return True
    else:
        return False
jefe_departamento.is_safe = True 
register.filter(jefe_departamento)

def por_aprobar(request):
    import pdb
    #pdb.set_trace()
    from django_messages.models import Message
    message_list = Message.objects.filter(status__nombre__iexact='En espera')
    return message_list 
por_aprobar.is_safe = True 
register.filter(por_aprobar)

def num_por_aprobar(request):
    return por_aprobar(request).count() 
num_por_aprobar.is_safe = True 
register.filter(num_por_aprobar)

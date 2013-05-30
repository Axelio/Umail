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

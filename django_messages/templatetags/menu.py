# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape
from django.utils.html import format_html

register = template.Library()
def menu(seccion):
    renderizar = ''

    titulos = []
    enlace = []
    vmenu=[]

    # Inicio
    titulos.append("Inicio")
    enlace.append("/")

    # Memos
    titulos.append("Memos")
    enlace.append("/entrada")

    # Project
    titulos.append("Project")
    enlace.append("/#")

    # Partners
    titulos.append("Partners")
    enlace.append("/#")

    # Noticias
    titulos.append("Noticias")
    enlace.append("/noticias")

    # Contact
    titulos.append("Contact")
    enlace.append("/#")

    vmenu.append(titulos)
    vmenu.append(enlace)

    clase = ''
    for posicion in range(titulos.__len__()):
        if titulos[posicion] == seccion:
            clase = 'class="current"'
        else:
            clase = ''
        url = '<li><a href='+ enlace[posicion] + " " + clase + '><span></span>' + titulos[posicion] + '</a></li>'
        renderizar = renderizar + url


    return format_html(renderizar)
menu.is_safe = True 
register.filter(menu)

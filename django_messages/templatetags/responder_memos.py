# -*- coding: utf8 -*-
from django import template
from django.utils.html import escape
from django.utils.html import format_html
from django_messages.models import Message
from auth.models import User

register = template.Library()
def responder_memo(memo,arg):
    memo = Message.objects.get(id=memo)
    user = User.objects.get(id=arg)
    respondercon_copia = False
    con_copia = False
    tabla = ''

    destinatario = memo.recipient

    if memo.recipient.usuarios.user.pk == user.pk and memo.con_copia == True:
        tabla = '<table></td><td width=100% align="left"><div class="rc_btn_02"><a href="/eliminar/' + str(memo.id) + '">Eliminar</a></div></td></tr></table>'
        con_copia=True

    if destinatario.grupos == None:

        if destinatario.usuarios.user.username == user.username and not con_copia:
            tabla = '<a href="/responder/' + str(memo.id) + '">Responder</a> <a href="/descargas/memo/' + str(memo.id) + '"Descargar</a><a href="/archivar/' + str(memo.id) + '" Archivar</a>'
    elif destinatario.usuarios == None:
        if user in destinatario.grupos.user_set.get_query_set():
            tabla = '<a href="/responder/' + str(memo.id) + '" Responder</a> <a href="/archivar/' + str(memo.id) + '" Archivar</a>'
    return format_html(tabla)
responder_memo.is_safe = True 
register.filter(responder_memo)


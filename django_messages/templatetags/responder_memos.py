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

    for dest in memo.con_copia.get_query_set():
        if dest.usuarios.user.pk == user.pk:
            tabla = '<table></td><td width=100% align="left"><div class="rc_btn_02"><a href="/eliminar/' + str(memo.id) + '">Eliminar</a></div></td></tr></table>'
            con_copia=True

    for destinatario in memo.recipient.get_query_set():
        if destinatario.grupos == None:

            if destinatario.usuarios.user.username == user.username and not con_copia:
                tabla = '<table><tr><td width=20%><a href="/responder/' + str(memo.id) + '" class="button"><span><span>Responder</span></span></a></div></td><td width=20% align="left"><a href="/memo/' + str(memo.id) + '" class="button"><span><span>Descargar</span></span></a></div></td><td width=20% align="left"><a href="/archivar/' + str(memo.id) + '" class="button"><span><span>Archivar</span></span></a></div></td></table>'
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                tabla = '<table><tr><td width=50%><a href="/responder/' + str(memo.id) + '" class="button"><span><span>Responder</span></span></a></div></td><td width=50% align="left"><a href="/eliminar/' + str(memo.id) + '" class="button"><span><span>Eliminar</span></span></a></div></td><td width=50% align="left"></td></tr></table>'
    return format_html(tabla)
responder_memo.is_safe = True 
register.filter(responder_memo)

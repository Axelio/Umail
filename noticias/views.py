# Create your views here.
from noticias.models import *
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

@login_required
def todas_noticias(request):
    diccionario = {}
    diccionario.update(csrf(request))
    noticias = Noticias.objects.all()
    diccionario.update({'noticias':noticias})
    return render_to_response('user/noticias/todas.html', diccionario)

@login_required
def detalle_noticia(request, noticia_id):
    diccionario = {}
    diccionario.update(csrf(request))
    noticias = Noticias.objects.filter(id=noticia_id)
    diccionario.update({'noticia_exists':noticias.exists()})
    if noticias.exists():
        diccionario.update({'noticia':noticias[0]})
    return render_to_response('user/noticias/especificas.html', diccionario)


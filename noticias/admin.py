#-*- coding: UTF8 -*-
from django.contrib import admin
from lib import admin as Autocompletar
from django.contrib import admin
from noticias.models import *

class NoticiasAdmin(admin.ModelAdmin):
    search_fields   = ('titulo','texto')
    list_display    = ('titulo','fecha') 
    list_filter     = ('fecha',)
admin.site.register(Noticias, NoticiasAdmin)

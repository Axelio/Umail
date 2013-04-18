#-*- coding: UTF8 -*-
from django.db import models

# Create your models here.
class Noticias(models.Model):
    titulo = models.CharField(max_length=300, verbose_name=u'título')
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table            = u'noticias'
        verbose_name_plural = u'noticias'
        verbose_name        = u'noticias'
    def __unicode__(self):
        return u'%s - %s' %(self.titulo, self.texto)

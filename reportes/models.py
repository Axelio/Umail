# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from auth.models import UserProfile

class Comentarios(models.Model):
    pregunta = models.CharField(max_length=50)
    comentario = models.TextField()
    nombre = models.CharField(max_length=50, verbose_name=u"nombre y apellido")
    correo = models.EmailField()
    class Meta:
        db_table            = u'comentarios'
        verbose_name_plural = u'comentarios'
    def __unicode__(self):
        return u'%s: %s'%(self.correo, self.pregunta)

class Respuestas(models.Model):
    pregunta = models.ForeignKey('Comentarios', editable=False)
    comentario = models.TextField()
    usuario = models.ForeignKey(UserProfile, null=True, blank=True, editable=False)
    respondido = models.BooleanField(default=False, editable=False)
    class Meta:
        db_table            = u'respuestas'
        verbose_name_plural = u'respuestas'
    def __unicode__(self):
        return u'%s'%(self.pregunta)

@receiver(post_save, sender=Respuestas)
def save_response(sender, **kwargs):
    from lib.umail import enviar_email

    respuesta = kwargs['instance']
    if respuesta.respondido == False:
        respuesta.respondido = True

    # Enviar correo de respuesta
    asunto = u'Respuesta a "%s"'%(respuesta.pregunta.pregunta)
    contenido = u'Uno de nuestros administradores ha respondido a su pregunta "%s" con el siguiente contenido: \n\n%s' %(respuesta.pregunta.pregunta, respuesta.comentario)
    enviar_email(asunto=asunto, contenido=contenido, correos=(respuesta.pregunta.correo,))

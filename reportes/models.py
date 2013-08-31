# -*- coding: utf8 -*-
from django.db import models

# Create your models here.
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
class Comentarios(models.Model):
    SENT_OPC = (
            ('FELIZ', 'Feliz'),
            ('MOLESTO', 'Molesto'),
            ('CONFUNDIDO', 'Confundido'),
            ('IMPRESIONADO', 'Impresionado'),
            ('SORPRENDIDO', 'Sorprendido'),
            ('DECEPCIONADO', 'Decepcionado'),
            ('FRUSTRADO', 'Frustrado'),
            ('CURIOSO', 'Curioso'),
            ('INDIFERENTE', 'Indiferente'),
                )

    #sentimiento = models.CharField(max_length=12, choices=SENT_OPC, blank=True, null=True)
    pregunta = models.CharField(max_length=50)
    comentario = models.TextField()
    nombre = models.CharField(max_length=50, verbose_name=u"nombre y apellido")
    correo = models.EmailField()
    class Meta:
        db_table            = u'comentarios'
        verbose_name_plural = u'comentarios'
    def __unicode__(self):
        return u'%s: %s'%(self.correo, self.pregunta)

@receiver(post_save, sender=Comentarios)
def enviar_mail_comentarios(sender, **kwargs):
    ''' Envío de memos a los admin del proyecto '''
    from umail.settings import ADMINS
    from django.core.mail import send_mail
    comentario = kwargs['instance']

    correos = []
    for admin in ADMINS:
        if  admin.__contains__('@') and admin.__contains__('.'):
            correos.append(admin)
    contenido = ''
    if correos:
        contenido = u'Tiene un comentario de %s preguntando %s con el siguiente mensaje: %s' %(comentario.correo, comentario.pregunta, comentario.comentario)
        send_mail('Comentario Umail', contenido, 'umail.unerg@gmail.com',
                correos, fail_silently=False)


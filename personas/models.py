# -*- coding: utf8 -*-
from django.db import models
from sedes.models import Niveles
from django.dispatch import receiver
from django.db.models.signals import post_save

# Modelo para aplicación de personas
class Personas(models.Model):
    from auth.models import Group
    tipodoc                 = models.CharField(choices=(('c','Cédula'),('p','Pasaporte')),default=0,max_length=1, verbose_name=u'Tipo de Identificación')
    num_identificacion      = models.CharField(max_length=50,unique=True,verbose_name=u'Número de Identificación')
    primer_apellido         = models.CharField(max_length=100)
    segundo_apellido        = models.CharField(max_length=100,blank=True)
    primer_nombre           = models.CharField(max_length=100)
    segundo_nombre          = models.CharField(max_length=100,blank=True)
    genero                  = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino')),default=0,verbose_name=u'sexo')
    email                   = models.EmailField()
    telefono                = models.IntegerField(unique=True, null=True, blank=True, help_text='Por favor, incluya el código de telefonía o área.')
    cargo_principal         = models.ForeignKey(Group,related_name=u'cargo_principal')
    cargos_autorizados      = models.ManyToManyField(Group, null=True, blank=True, default=None, related_name=u'cargos_autorizados')
    class Meta:
        db_table            = u'personas'
        verbose_name_plural = u'personas'
    def __unicode__(self):
        return u'%s %s'%(self.primer_nombre,self.primer_apellido)

@receiver(post_save, sender=Personas)
def save_pers_user(sender, **kwargs):
    ''' Guardar en la tabla Destinatarios el usuario creado '''
    from django.contrib.auth.models import User
    from auth.models import UserProfile
    from django_messages.models import Destinatarios
    persona = kwargs['instance']
    usuario = User.objects.filter(models.Q(username=persona.email)|models.Q(email=persona.email))
    usuario_perfil = UserProfile.objects.filter(user=usuario)
    if not usuario.exists():
        usuario = User.objects.create_user(username = persona.email, email = persona.email, password = persona.num_identificacion)
        if not usuario_perfil.exists():
            usuario_perfil = UserProfile.objects.create(persona=persona, user=usuario)
        else:
            usuario_perfil = usuario_perfil[0]
    else:
        usuario = usuario[0]
        if not usuario_perfil.exists():
            usuario_perfil = UserProfile.objects.create(persona=persona, user=usuario)
        else:
            usuario_perfil = usuario_perfil[0]

    # Guardar al usuario en el grupo donde desempeñe el cargo principal
    usuario.groups.add(persona.cargo_principal.id)

    usuario.first_name = persona.primer_nombre
    usuario.last_name = persona.primer_apellido
    usuario.is_staff = True
    usuario.save()
    destinatario = Destinatarios.objects.get_or_create(usuarios=usuario_perfil)

class Cargos(models.Model):
    nombre                  = models.CharField(max_length=200, unique=True)
    nivel                   = models.ForeignKey(Niveles)
    class Meta:
        db_table            = u'cargos'
        verbose_name_plural = u'cargos'
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Permisos(models.Model):
    nombre                  = models.CharField(max_length=50)
    nivel                   = models.IntegerField(help_text=u'De menor a mayor, el nivel de acceso que tiene %s' %(nombre))
    class Meta:
        db_table            = u'permisos'
        verbose_name_plural = u'permisos'
        verbose_name        = u'permiso'
    def __unicode__(self):
        return '%s' (self.nombre)

class Autoridades(models.Model):
    persona                 = models.ForeignKey('Personas')
    tipo_personal           = models.ForeignKey('TipoPersonal')
    #dependencia             = models.ForeignKey(Dependencias)
    class Meta:
        db_table            = u'autoridades'
        verbose_name_plural = u'autoridades'
        verbose_name        = u'autoridad'
    def __unicode__(self):
        return '%s - %s' (self.persona, self.dependencia)

class TipoPersonal(models.Model):
    nombre                  = models.CharField(max_length=50)
    class Meta:
        db_table            = u'tipo_personal'
        verbose_name_plural = u'tipos de personal'
        verbose_name        = u'tipo de personal'
    def __unicode__(self):
        return '%s' %(self.nombre)

# -*- coding: utf8
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model
from sedes.models import Personas
from django.core.validators import email_re

class UserModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        #Se introdujo un correo?
        if email_re.search(username): #Se introdujo un correo?
            try:
                #Evalua si hay una Persona con ese email a través de la relación del perfil de usuario (userprofile)
                user=User.objects.get(userprofile__persona__email=username)
            except :
                try:
                    #Evaluar si hay un user (admin?) con ese correo
                    user = User.objects.get(email=username)
                    
                except User.DoesNotExist:
                    #no existe
                    return None 
                
        else: #se introdujo un nombre de usuario?
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
#'            return self.user_class.objects.get(pk=user_id)
            return User.objects.get(pk=user_id)
        except:
            return None

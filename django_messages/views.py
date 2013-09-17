# -*- coding: utf-8 -*-
import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from lib.umail import msj_expresion, renderizar_plantilla
from django.utils.translation import ugettext as _
from django.utils import simplejson
from django.http import HttpResponse
from django.utils.translation import ugettext_noop
from django.db.models import Q
from django_messages.models import Destinatarios, EstadoMemo
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_messages.models import Message
from django_messages.forms import ComposeForm, BandejaForm
from django_messages.utils import format_quote
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, DELETION, CHANGE
from django.forms.models import modelformset_factory
from umail import settings

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

def anular(request, message_id):
    if request.user.profile.persona.cargo_principal.cargo == request.user.profile.persona.cargo_principal.dependencia.cargo_max:
        from django_messages.models import EstadoMemo
        mensaje = Message.objects.get(id=message_id)
        estado = EstadoMemo.objects.get(nombre='Anulado')
        mensaje.status = estado
        mensaje.save()
        return por_aprobar(request, mensaje=u'Memorándum anulado exitosamente')
    else:
        raise Http404
anular = login_required(anular, login_url='/auth')


def aprobar(request, message_id):
    if request.user.profile.persona.cargo_principal.cargo == request.user.profile.persona.cargo_principal.dependencia.cargo_max:
        from django_messages.models import EstadoMemo, Destinatarios
        mensaje = Message.objects.get(id=message_id)
        estado = EstadoMemo.objects.get(nombre='Aprobado')
        mensaje.status = estado
        mensaje.save()
        return por_aprobar(request, mensaje=u'Memorándum aprobado exitosamente')
    else:
        raise Http404
aprobar = login_required(aprobar, login_url='/auth')

def por_aprobar(request, mensaje=''):
    """
    Displays a list of received messages for the current user.
    Optional Arguments:
        ``template_name``: name of the template to use.
    """
    notify = False
    if not mensaje == '':
        notify = True
    if request.user.is_authenticated():
        dependencia = request.user.profile.persona.cargo_principal.dependencia
        # Lista de mensajes en espera escritos por la dependencia del jefe de dependencia
        message_list = Message.objects.filter(models.Q( status__nombre__iexact='En espera', 
                                                        sender__usuarios__persona__cargo_principal__dependencia=dependencia)| 
                                              models.Q(sender__usuarios__persona__cargos_autorizados__dependencia=dependencia))
        if not message_list.exists():
            mensaje = u'No tiene ningún mensaje por aprobar hasta ahora'
        return render_to_response('user/mensajes/bandeja.html', {
            'message_list': message_list,
            'loggeado': request.user.is_authenticated,
            'request':request,
            'mensaje':mensaje,
            'notify':notify,
        }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def ver_por_aprobar(request, message_id, template_name='user/mensajes/leer_aprobado.html'):
    """
    Shows a single message.``message_id`` argument is required.
    The user is only allowed to see the message, if he is either 
    the sender or the recipient. If the user is not allowed a 404
    is raised. 
    If the user is the recipient and the message is unread 
    ``read_at`` is set to the current datetime.
    """
    user = request.user
    if user.profile.persona.cargo_principal.cargo == user.profile.persona.cargo_principal.dependencia.cargo_max:
        now = datetime.datetime.now()
        message = get_object_or_404(Message, id=message_id)
        esta_destinatario = False
        
        message_list = Message.objects.filter(models.Q(status__nombre__iexact='En espera', sender__usuarios__persona__cargo_principal__dependencia=request.user.profile.persona.cargo_principal.dependencia)| models.Q(sender__usuarios__persona__cargos_autorizados__dependencia=request.user.profile.persona.cargo_principal.dependencia))

    else:
        raise Http404

    return render_to_response(template_name, {
        'loggeado': request.user.is_authenticated,
        'request':request,
        'message': message,
        'message_list': message_list,
    }, context_instance=RequestContext(request))
ver_por_aprobar = login_required(ver_por_aprobar, login_url='/auth')

def bandeja(request, tipo_bandeja='', expresion='', tipo_mensaje='', mensaje=''):
    """
    Displays a list of received messages for the current user.
    Optional Arguments:
        ``template_name``: name of the template to use.
    """
    notify = False
    diccionario = {}
    diccionario.update(csrf(request))
    if request.user.is_authenticated():
        if request.method == "POST":
            form = BandejaForm(request.POST)
            now = datetime.datetime.now()
            # Revisar si hay POST con archivar
            if request.POST.has_key('archivar'):
                lista = request.POST.getlist('seleccion')
                if lista.__len__() == 0:
                    form.errors.update({'mensajes':u'No seleccionó ningún mensaje'})
                    tipo_mensaje = 'error'
                    mensaje = form.errors['mensajes']
                else:
                    lista_memos = []
                    for num in lista:
                        lista_memos.append(int(num))

                    # Buscar los memos según los ids que llegan
                    lista_memos = Message.objects.filter(id__in=lista_memos)

                    total_memos = lista_memos.count()
                    if lista_memos.exclude(status__nombre = 'En espera').count() == total_memos:
                        tipo_mensaje = 'success'
                        mensaje = 'Un total de %s mensajes fueron archivados.' %(total_memos)
                    else:
                        tipo_mensaje = 'error'
                        mensaje = 'Los memos en espera que no pueden ser archivados. '
                        if lista_memos.exclude(status__nombre = 'En espera').count() > 1:
                            mensaje = mensaje + 'Sin embargo, %s memos fueron archivados' %(lista_memos.exclude(status__nombre = 'En espera').count())
                        elif lista_memos.exclude(status__nombre = 'En espera').count() == 1:
                            mensaje = mensaje + 'Sin embargo, %s memo fue archivado.' %(lista_memos.exclude(status__nombre = 'En espera').count())

                    for memo in lista_memos.exclude(status__nombre = 'En espera'):
                        memo.deleted_at = now
                        # Guardar log de memo archivado
                        LogEntry.objects.create(
                        user_id         = request.user.pk, 
                        content_type_id = ContentType.objects.get_for_model(Message).id,
                        object_id       = memo.id,
                        object_repr     = repr(memo), 
                        change_message  = mensaje,
                        action_flag     = DELETION
                        )
                        memo.save()



                '''
                message = get_object_or_404(Message, id=message_id)
                deleted = False
                notify = False
                if success_url is None:
                    success_url = reverse('messages_inbox')
                if request.GET.has_key('next'):
                    success_url = request.GET['next']
                if message.sender.usuarios.user == user:
                    message.sender_deleted_at = now
                    deleted = True
                for destinatario in message.recipient.get_query_set():
                    if destinatario.grupos == None:
                        if destinatario.usuarios.user.username == user.username:
                            message.recipient_deleted_at = now
                            deleted = True
                    elif destinatario.usuarios == None:
                        if user in destinatario.grupos.user_set.get_query_set():
                            message.recipient_deleted_at = now
                            deleted = True
                if deleted:
                    if message.status == 'En espera':
                        message.save()
                        mensaje_txt = u"Mensaje archivado exitosamente."

                        # Guardar log de memo archivado
                        LogEntry.objects.create(
                        user_id         = request.user.pk, 
                        content_type_id = ContentType.objects.get_for_model(Message).id,
                        object_id       = message.id,
                        object_repr     = repr(message), 
                        change_message  = mensaje_txt,
                        action_flag     = DELETION
                        )
                        mensaje = mensaje_txt
                    else:
                        mensaje = u'Un mensaje que está en espera de ser aprobado no puede ser archivado aún.'
                    notify = True
                    if notification:
                        notification.send([user], "messages_deleted", {'message': message,})
                    return inbox(request, mensaje)
                raise Http404
                '''










        form = BandejaForm()

        if tipo_bandeja == 'enviados': # ENVIADOS
            message_list = Message.objects.outbox_for(request.user).distinct() #Filtrando la bandeja
        if tipo_bandeja == 'entrada': # ENTRADA
            message_list = Message.objects.inbox_for(request.user).distinct() #Filtrando la bandeja

        if not message_list.exists() and mensaje == '':
            mensaje = u'No tiene ningún mensaje hasta ahora'
            (tipo_mensaje, expresion) = msj_expresion('info')
        
        paginador = Paginator(message_list, settings.SUIT_CONFIG['LIST_PER_PAGE'])
        page = request.GET.get('page')
        try:
            message_list = paginador.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            message_list = paginador.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            message_list = paginador.page(paginator.num_pages)

        diccionario.update({'request':request})
        diccionario.update({'message_list':message_list})
        diccionario.update({'tipo_mensaje':tipo_mensaje})
        diccionario.update({'expresion':expresion})
        diccionario.update({'mensaje':mensaje})
        diccionario.update({'tipo_bandeja':tipo_bandeja})
        return render_to_response('usuario/mensajes/bandejas.html', diccionario, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def outbox(request, mensaje='', template_name='usuario/mensajes/bandejas.html'):
    """
    Displays a list of sent messages by the current user.
    Optional arguments:
        ``template_name``: name of the template to use.
    """
    message_list = Message.objects.outbox_for(request.user)
    mensajes = message_list
    paginador = Paginator(message_list, 20)
    page = request.GET.get('page')
    try:
        message_list = paginador.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        message_list = paginador.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        message_list = paginador.page(paginator.num_pages)
    if not mensajes.exists():
        mensaje = u'No tiene ningún mensaje hasta ahora'
    return render_to_response(template_name, {
        'request':request,
        'mensaje':mensaje,
        'message_list': message_list,
        'tipo_bandeja':'enviados',
    }, context_instance=RequestContext(request))
outbox = login_required(outbox, login_url='/auth')

def trash(request, template_name='user/mensajes/bandeja.html', mensaje=''):
    """
    Displays a list of deleted messages. 
    Optional arguments:
        ``template_name``: name of the template to use
    Hint: A Cron-Job could periodicly clean up old messages, which are deleted
    by sender and recipient.
    """
    message_list = Message.objects.trash_for(request.user)
    mensajes = message_list
    paginador = Paginator(message_list, 20)
    page = request.GET.get('page')
    try:
        message_list = paginador.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        message_list = paginador.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        message_list = paginador.page(paginator.num_pages)
    if not mensajes.exists():
        mensaje = u'No tiene ningún mensaje hasta ahora'
    return render_to_response(template_name, {
        'message_list': message_list,
        'mensaje':mensaje,
        'request':request,
    }, context_instance=RequestContext(request))
trash = login_required(trash, login_url='/auth')

def compose(request, recipient=None,
        template_name='usuario/mensajes/redactar.html', success_url=None, recipient_filter=None):
    """
    Displays and handles the ``form_class`` form to compose new messages.
    Required Arguments: None
    Optional Arguments:
        ``recipient``: username of a `django.contrib.auth` User, who should
                       receive the message, optionally multiple usernames
                       could be separated by a '+'
        ``form_class``: the form-class to use
        ``template_name``: the template to use
        ``success_url``: where to redirect after successfull submission
    """
    form_errors = ''
    if request.method == "POST":
        form = ComposeForm(request.POST)
        cuerpo = ''
        valido = form.is_valid()

        # Revisar si hay quien apruebe en el departamento del redactor
        jefe = Destinatarios.objects.filter(usuarios__user__userprofile__persona__cargo_principal__dependencia = request.user.profile.persona.cargo_principal.dependencia, usuarios__user__userprofile__persona__cargo_principal__cargo = request.user.profile.persona.cargo_principal.dependencia.cargo_max)
        if not jefe.exists():
            mensaje = u'Este memo no puede ser enviado ni aprobado porque no existe un jefe de departamento en %s' %(request.user.profile.persona.cargo_principal.dependencia)
            valido = False
        else:
            jefe = jefe[0]

        if valido:
            destinatarios = form.cleaned_data['recipient']

            mensaje_txt = u'Mensaje enviado exitosamente'

            # Por cada destinatario, enviar el memo, generar un log y enviar correo si está en la opción de envío
            estado_memo = EstadoMemo.objects.get(nombre='En espera')
            for destino in destinatarios:

                # Crear el mensaje a todas las personas en estado 'En espera'
                mensaje = Message.objects.create(
                                sender = Destinatarios.objects.get(usuarios__user=request.user),
                                recipient = destino,
                                subject = request.POST['subject'],
                                body = request.POST['body'],
                                status = estado_memo,
                                tipo = ' ',
                            )

                # Guardar log de envío de memo
                LogEntry.objects.create(
                    user_id         = request.user.pk, 
                    content_type_id = ContentType.objects.get_for_model(Message).id,
                    object_id       = mensaje.id,
                    object_repr     = repr(mensaje), 
                    change_message  = mensaje_txt,
                    action_flag     = ADDITION
                )

            if not destinatarios.__contains__(jefe):
                # Crear el mensaje al jefe de la dependencia
                mensaje = Message.objects.create(
                                sender = Destinatarios.objects.get(usuarios__user=request.user),
                                recipient = jefe,
                                subject = request.POST['subject'],
                                body = request.POST['body'],
                                status = estado_memo,
                                tipo = ' ',
                            )

                # Guardar log de envío de memo
                LogEntry.objects.create(
                    user_id         = request.user.pk, 
                    content_type_id = ContentType.objects.get_for_model(Message).id,
                    object_id       = mensaje.id,
                    object_repr     = repr(mensaje), 
                    change_message  = mensaje_txt,
                    action_flag     = ADDITION
                )

            mensaje = mensaje_txt
            (tipo_mensaje, expresion) = msj_expresion('success')

            if success_url is None:
                success_url = reverse('messages_inbox')
            if request.GET.has_key('next'):
                success_url = request.GET['next']

        if form.errors or not valido:
            (tipo_mensaje, expresion) = msj_expresion('error')
            label = ""
            if form.errors.keys()[0] == 'subject':
                label = "Asunto"
            elif form.errors.keys()[0] == 'recipient':
                label = "Destinatarios"
            elif form.errors.keys()[0] == 'body':
                label = "Texto"

            if not label == "":
                mensaje =  label + ': ' + form.errors.values()[0][0]

        return bandeja(request, tipo_bandeja='entrada', expresion=expresion, tipo_mensaje=tipo_mensaje, mensaje=mensaje)
    else:
        form = ComposeForm()
        cuerpo = form.fields['body'].initial = u"\n\nCordialmente, \n%s. %s de %s" %(request.user.profile.persona, request.user.profile.persona.cargo_principal.cargo, request.user.profile.persona.cargo_principal.dependencia)
        if recipient is not None:
            recipients = [u for u in User.objects.filter(username__in=[r.strip() for r in recipient.split('+')])]
            form.fields['recipient'].initial = recipients
    return render_to_response(template_name, {
        'cuerpo': cuerpo,
        'tipo': 'Redactar',
        'form_errors':form_errors,
        'request': request,
        'form': form,
    }, context_instance=RequestContext(request))
compose = login_required(compose, login_url='/auth')

def reply(request, message_id, form_class=ComposeForm,
    template_name='user/mensajes/redactar.html', success_url=None, 
        recipient_filter=None, quote_helper=format_quote):
    """
    Prepares the ``form_class`` form for writing a reply to a given message
    (specified via ``message_id``). Uses the ``format_quote`` helper from
    ``messages.utils`` to pre-format the quote. To change the quote format
    assign a different ``quote_helper`` kwarg in your url-conf.
    
    """
    parent = get_object_or_404(Message, id=message_id)
    
    user = request.user
    now = datetime.datetime.now()
    esta_destinatario = False

    for destinatario in parent.con_copia.get_query_set():
        if destinatario.grupos == None:
            if destinatario.usuarios.user == user:
                esta_destinatario = True
                continue
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                esta_destinatario = True
                continue

    for destinatario in parent.recipient.get_query_set():
        if destinatario.grupos == None:
            if destinatario.usuarios.user == user:
                esta_destinatario = True
                continue
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                esta_destinatario = True
                continue

    if (parent.sender != user) and (esta_destinatario == False):
        raise Http404
    
    if request.method == "POST":
        sender = request.user
        form = form_class(request.POST)
        if form.is_valid():
            estado_memo = EstadoMemo.objects.get(nombre='En espera')
            mensaje = Message(
                            sender = Destinatarios.objects.get(usuarios__user=request.user),
                            subject = request.POST['subject'],
                            body = request.POST['body'],
                            status = estado_memo,
                            parent_msg = parent,
                        )
            mensaje.save()
            dest = []
            for i in request.POST['recipient'].split('|'):
                if not i == '':
                    dest.append(int(i))
            for destin in dest:
                sender = Destinatarios.objects.filter(id=destin)
                if sender.exists():
                    mensaje.recipient.add(sender[0])
            mensaje.save()
            mensaje_txt = u"Mensaje enviado exitosamente."

            # Guardar log de envío de memo
            LogEntry.objects.create(
            user_id         = request.user.pk, 
            content_type_id = ContentType.objects.get_for_model(Message).id,
            object_id       = mensaje.id,
            object_repr     = repr(mensaje), 
            change_message  = mensaje_txt,
            action_flag     = ADDITION
            )
            mensaje = mensaje_txt

                    
            return inbox(request, mensaje)
    else:
        cuerpo = u"\n\n%s escribió:\n%s" %(parent.sender, parent.body)
        recipient = parent.recipient.add(parent.sender)
        destins = []
        for recip in parent.recipient.get_query_set():
            destins.append(recip.id)
        form = form_class(initial={
            'subject': _(u"Re: %(subject)s") % {'subject': parent.subject},
            'body': cuerpo,
            'recipient': destins
            })
    return render_to_response(template_name, {
        'tipo': 'Responder',
        'request': request,
        'form': form,
    }, context_instance=RequestContext(request))
reply = login_required(reply, login_url='/auth')

def delete(request, message_id, success_url=None):
    """
    Marks a message as deleted by sender or recipient. The message is not
    really removed from the database, because two users must delete a message
    before it's save to remove it completely. 
    A cron-job should prune the database and remove old messages which are 
    deleted by both users.
    As a side effect, this makes it easy to implement a trash with undelete.
    
    You can pass ?next=/foo/bar/ via the url to redirect the user to a different
    page (e.g. `/foo/bar/`) than ``success_url`` after deletion of the message.
    """
    user = request.user
    now = datetime.datetime.now()
    message = get_object_or_404(Message, id=message_id)
    deleted = False
    notify = False
    if success_url is None:
        success_url = reverse('messages_inbox')
    if request.GET.has_key('next'):
        success_url = request.GET['next']
    if message.sender.usuarios.user == user:
        message.sender_deleted_at = now
        deleted = True
    for destinatario in message.recipient.get_query_set():
        if destinatario.grupos == None:
            if destinatario.usuarios.user.username == user.username:
                message.recipient_deleted_at = now
                deleted = True
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                message.recipient_deleted_at = now
                deleted = True
    if deleted:
        if message.status == 'En espera':
            message.save()
            mensaje_txt = u"Mensaje archivado exitosamente."

            # Guardar log de memo archivado
            LogEntry.objects.create(
            user_id         = request.user.pk, 
            content_type_id = ContentType.objects.get_for_model(Message).id,
            object_id       = message.id,
            object_repr     = repr(message), 
            change_message  = mensaje_txt,
            action_flag     = DELETION
            )
            mensaje = mensaje_txt
        else:
            mensaje = u'Un mensaje que está en espera de ser aprobado no puede ser archivado aún.'
        notify = True
        if notification:
            notification.send([user], "messages_deleted", {'message': message,})
        return inbox(request, mensaje)
    raise Http404
delete = login_required(delete, login_url='/auth')

def undelete(request, success_url=None):
    """
    Recovers a message from trash. This is achieved by removing the
    ``(sender|recipient)_deleted_at`` from the model.
    """
    user = request.user
    message = get_object_or_404(Message, id=message_id)
    undeleted = False
    if success_url is None:
        success_url = reverse('messages_inbox')
    if request.GET.has_key('next'):
        success_url = request.GET['next']
    if message.sender == user:
        message.sender_deleted_at = None
        undeleted = True
    if message.recipient == user:
        message.recipient_deleted_at = None
        undeleted = True
    if undeleted:
        message.save()
        messages.info(request, _(u"Message successfully recovered."))
        if notification:
            notification.send([user], "messages_recovered", {'message': message,})
        return HttpResponseRedirect(success_url)
    raise Http404
undelete = login_required(undelete, login_url='/auth')

def view(request, message_id, template_name='user/mensajes/leer.html', mensaje=''):
    """
    Shows a single message.``message_id`` argument is required.
    The user is only allowed to see the message, if he is either 
    the sender or the recipient. If the user is not allowed a 404
    is raised. 
    If the user is the recipient and the message is unread 
    ``read_at`` is set to the current datetime.
    """
    user = request.user
    now = datetime.datetime.now()
    message = get_object_or_404(Message, id=message_id)
    esta_destinatario = False

    for destinatario in message.con_copia.get_query_set():
        if destinatario.grupos == None:
            if destinatario.usuarios.user == user:
                esta_destinatario = True
                continue
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                esta_destinatario = True
                continue

    for destinatario in message.recipient.get_query_set():
        if destinatario.grupos == None:
            if destinatario.usuarios.user == user:
                esta_destinatario = True
                continue
        elif destinatario.usuarios == None:
            if user in destinatario.grupos.user_set.get_query_set():
                esta_destinatario = True
                continue

    from django_messages.models import Destinatarios
    destin = Destinatarios.objects.get(usuarios__user=user)
    jefe = Destinatarios.objects.get(usuarios__user__userprofile__persona__cargo_principal__dependencia = message.sender.usuarios.user.profile.persona.cargo_principal.dependencia, usuarios__user__userprofile__persona__cargo_principal__cargo = message.sender.usuarios.user.profile.persona.cargo_principal.dependencia.cargo_max)

    # Si el usuario no esta entre los destinatarios, y el mensaje no lo envia el usuario y el usuario no es el jefe del que redacto el mensaje
    if not message.sender == destin and not esta_destinatario and not user == jefe.usuarios.user:
        raise Http404

    else:
        if message.status.nombre == 'Aprobado':
            message.read_at = now
            
            if message.sender != destin and not user == jefe.usuarios.user: 
                message.leido_por.add(destin)
            if message.sender in message.leido_por.get_query_set():
                message.leido_por.remove(destin)
            mensaje=message
            mensaje.save()
            mensaje_txt = u"Mensaje nuevo leído."

            # Guardar log de memo archivado
            LogEntry.objects.create(
            user_id         = request.user.pk, 
            content_type_id = ContentType.objects.get_for_model(Message).id,
            object_id       = mensaje.id,
            object_repr     = repr(mensaje), 
            change_message  = mensaje_txt,
            action_flag     = CHANGE
            )

    return render_to_response(template_name, {
        'loggeado': request.user.is_authenticated,
        'request':request,
        'jefe':jefe,
        'message': message,
    }, context_instance=RequestContext(request))
view = login_required(view, login_url='/auth')

def destin_atarios_lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = Message.objects.filter(subject__istartswith=value)
                results = [ x.subject for x in model_results ]
                print results
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')

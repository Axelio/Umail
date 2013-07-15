# -*- coding: utf-8 -*-
import datetime
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_noop
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django_messages.models import Message
from django_messages.forms import ComposeForm
from django_messages.utils import format_quote
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, DELETION, CHANGE

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
anular = login_required(anular)


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
aprobar = login_required(aprobar)

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
        message_list = Message.objects.filter(
                                              models.Q( status__nombre__iexact='En espera', 
                                                        sender__usuarios__persona__cargo_principal__dependencia=dependencia)| 
                                              models.Q(sender__usuarios__persona__cargos_autorizados__dependencia=dependencia))
        if not message_list.exists():
            mensaje = u'No tiene ningún mensaje por aprobar hasta ahora'
        return render_to_response('user/mensajes/por_aprobar.html', {
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
ver_por_aprobar = login_required(ver_por_aprobar)

def inbox(request, mensaje=''):
    """
    Displays a list of received messages for the current user.
    Optional Arguments:
        ``template_name``: name of the template to use.
    """
    notify = False
    if not mensaje == '':
        notify = True
    if request.user.is_authenticated():
        message_list = Message.objects.inbox_for(request.user).distinct()
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
        return render_to_response('user/mensajes/bandeja.html', {
            'message_list': message_list,
            'request':request,
            'mensaje':mensaje,
            'notify':notify,
            'tipo_bandeja':'entrada',
        }, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')

def outbox(request, mensaje='', template_name='user/mensajes/bandeja.html'):
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
    }, context_instance=RequestContext(request))
outbox = login_required(outbox)

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
trash = login_required(trash)

def compose(request, recipient=None,
        template_name='user/mensajes/redactar.html', success_url=None, recipient_filter=None):
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
        from django_messages.models import Destinatarios
        if not Destinatarios.objects.filter(usuarios__user__userprofile__persona__cargo_principal__dependencia = request.user.profile.persona.cargo_principal.dependencia, usuarios__user__userprofile__persona__cargo_principal__cargo = request.user.profile.persona.cargo_principal.dependencia.cargo_max).exists():
            mensaje = u'Este memo no puede ser enviado ni aprobado porque no existe un jefe de departamento en %s' %(request.user.profile.persona.cargo_principal.dependencia)
            form_errors = mensaje
            valido = False
        if valido:
            from django_messages.models import Destinatarios, EstadoMemo
            estado_memo = EstadoMemo.objects.get(nombre='En espera')
            #form = form_class(request.POST)
            #form = form_class(request.POST, recipient_filter=recipient_filter)
            mensaje = Message(
                            sender = Destinatarios.objects.get(usuarios__user=request.user),
                            subject = request.POST['subject'],
                            body = request.POST['body'],
                            status = estado_memo,
                            tipo = '',
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
            mensaje_txt = u'Mensaje enviado exitosamente'

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

            if success_url is None:
                success_url = reverse('messages_inbox')
            if request.GET.has_key('next'):
                success_url = request.GET['next']
            return inbox(request, mensaje)
    else:
        form = ComposeForm()
        cuerpo = form.fields['body'].initial = u"\n\nCordialmente, \n%s. %s de %s" %(request.user.profile.persona, request.user.profile.persona.cargo_principal.cargo, request.user.profile.persona.cargo_principal.dependencia)
        if recipient is not None:
            recipients = [u for u in User.objects.filter(username__in=[r.strip() for r in recipient.split('+')])]
            form.fields['recipient'].initial = recipients
    if form.errors:
        if form.errors.keys()[0] == 'subject':
            label = "Asunto"
        elif form.errors.keys()[0] == 'recipient':
            label = "Destinatarios"
        elif form.errors.keys()[0] == 'body':
            label = "Texto"
        form_errors =  label + ': ' + form.errors.values()[0][0]
    return render_to_response(template_name, {
        'cuerpo': cuerpo,
        'tipo': 'Redactar',
        'form_errors':form_errors,
        'request': request,
        'form': form,
    }, context_instance=RequestContext(request))
compose = login_required(compose)

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
            from django_messages.models import Destinatarios, EstadoMemo
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
reply = login_required(reply)

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
delete = login_required(delete)

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
undelete = login_required(undelete)

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
view = login_required(view)

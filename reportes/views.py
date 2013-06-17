#-*- coding: utf8  
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.db import transaction, models
from django.core import serializers
from django.core.context_processors import csrf
from lib import fecha
import datetime
from umail import settings
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT 
from reportlab.pdfgen import  canvas
from reportlab.platypus import SimpleDocTemplate, BaseDocTemplate, Image, Spacer, Paragraph, Table, TableStyle 
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm

PAGE_HEIGHT=29.7*cm
PAGE_WIDTH=21*cm

def memo(request, message_id):
    ''' Función para descarga de memorándums en PDF '''
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = u'attachment; filename=Memorándum.pdf; pagesize=A4'

    #elementos es la lista donde almaceno todos lo que voy a incluir al documento pdf
    elementos = []
    doc = SimpleDocTemplate(response)    
    style = getSampleStyleSheet() 
    style2 = getSampleStyleSheet()
    styleFecha = getSampleStyleSheet()
    styleEncabezado = getSampleStyleSheet()

    fechas = datetime.datetime.today()
    mes = fecha.NormalDate().monthName()
    dia = fecha.NormalDate().dayOfWeekName()

    txtFecha = '%s, %s DE %s DE %s'%(dia.upper(), fechas.day, mes.upper(), fechas.year)
    styleF = styleFecha['Normal']
    styleF.fontSize = 8
    styleF.fontName = 'Helvetica'
    styleF.alignment = TA_RIGHT
    fechaV = Paragraph(txtFecha, styleF)
    elementos.append(fechaV)
    elementos.append(Spacer(1,5))

    #-- Espacio para poner el encabezado con la clase Canvas
    elementos.append(Spacer(1,75))

    txtTitulo = u'LISTADO DE MEMORÁNDUM'
    titulo = style['Heading1']
    titulo.fontSize = 12
    titulo.fontName = 'Helvetica-Bold'
    titulo.alignment = TA_CENTER
    tituloV = Paragraph(txtTitulo, titulo)
    elementos.append(tituloV)
    elementos.append(Spacer(1,5))

    tablaLapso = []
    tablaEstudiantes = []
    tablaCarrera = []
    x = [
    ('BOX', (0,0), (-1,-1), 0.50, colors.black),
    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    #('TOPPADDING', (0,0), (-1,-1), 1),
    #('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ('GRID', (0,0), (-1,-1), 0.50, colors.black),
    #('FONT', (0,0), (-1,-1), "Helvetica", 8),
    ('FONT', (0,0), (-1,-1), "Helvetica", 6),
    ]

    TEXTO = 'Texto'


    tablaCarrera.append([u'ÁREA: %s'%(TEXTO), 'CARRERA: %s'%(TEXTO)])
    t3 = Table(tablaCarrera, colWidths=(7.5*cm, 7.5*cm))
    t3.setStyle(TableStyle(x))
    elementos.append(t3)
    elementos.append(Spacer(1,0.5))

    tablaLapso.append(['ASIGNATURA: %s'%(TEXTO), 'SEM.: %s'%(TEXTO), 'LAPSO: %s'%(TEXTO)])
    tablaLapso.append(['PROFESOR: %s '%(TEXTO)])

    t = Table(tablaLapso, colWidths=(8.2*cm, 1.8*cm, 5.0*cm))
    t.setStyle(TableStyle(x)) 
    elementos.append(t)
    elementos.append(Spacer(1,10))

    y = [
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('FONT', (0,0), (-1,-1), "Helvetica", 6),
    ('GRID', (0,0), (-1,-1), 0.60, colors.black),
    ('BOTTOMPADDING', (0,0), (3,0), 5),
    ('FONT', (0,0), (3,0), "Helvetica-Bold", 6),
    ('ALIGN', (1,1), (-1,-1), 'LEFT'),
    ]

    tablaEstudiantes.append(['NRO','CI', 'NOMBRES Y APELLIDOS', 'FIRMA'])
    # Empieza la tabla de los alumos.
    num = 0
    tablaEstudiantes.append(['%d'%(num),'%s'%(TEXTO), u'%s'%(TEXTO), ''])
    
    t2 = Table(tablaEstudiantes, colWidths=('',1.8*cm, 8.8*cm, 3.5*cm))
    t2.setStyle(TableStyle(y))
    elementos.append(t2)

    doc.build(elementos, canvasmaker=NumeroDePagina, onFirstPage=encabezado_constancia)
    return response  
memo = login_required(memo)

def encabezado_constancia(canvas, doc):
    canvas.saveState()
    canvas.drawImage(settings.STATIC_ROOT+'images/unerg.jpg', 2.6*cm, PAGE_HEIGHT-4.5*cm, width = 100, height = 38)
    canvas.setFont("Helvetica-Bold",9)
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-3.6*cm, u'REPÚBLICA BOLIVARIANA DE VENEZUELA')
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-4.0*cm, u'UNIVERSIDAD NACIONAL EXPERIMENTAL RÓMULO GALLEGOS')
    canvas.drawCentredString(PAGE_WIDTH-9.5*cm, PAGE_HEIGHT-4.4*cm, u'DIRECCIÓN DE ADMISIÓN, CONTROL Y EVALUACIÓN')
    canvas.restoreState()
    canvas.saveState()

class NumeroDePagina(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        fechas = datetime.datetime.today()
        self.setFont("Helvetica-Bold", 6)
        self.drawRightString(129*mm, 6*mm,
            u"D.A.C.E     %02d/%02d/%d   %02d:%02d:%02d    Página %d de %d" % (fechas.day,fechas.month,fechas.year, fechas.hour, fechas.minute, fechas.second, self._pageNumber, page_count))


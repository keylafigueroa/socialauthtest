from django import forms
from django.core.context_processors import request
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth.models import *
from django.utils import simplejson
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Q
from espe_app.models import *


def home(request):
    return render_to_response("inicio.html")

def privado(request):
    return render_to_response("private.html")

@csrf_exempt
def consultar_alumno_api(request):
    q=request.GET.get("q", "")
    p=request.GET.get("page", 0)
    alumnos=  Alumno.objects.filter(ci__icontains=q)[p:10]
    lista = map(lambda x:{
        "id": x.id, "cedula":x.ci, "nombre":x.nombre, "apellido":x.apellido, "anio":x.anio, "termino":x.termino,
        "cal1":x.cal1, "cal2":x.cal2, "cal3":x.cal3}, alumnos)
    data ={"lista": lista, "success":True}
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

@csrf_exempt
def consultar_noticias_api(request):
    q=request.GET.get("q", "")
    p=request.GET.get("page", 0)
    noticias=  Noticia.objects.filter(titulo__icontains=q, esta_publicado=True)[p:10]
    lista = map(lambda x:{
        "id": x.id, "titulo":x.titulo, "fecha_publicacion":x.fecha_publicacion.strftime('%m/%d/%Y'), "descripcion":x.descripcion
    }, noticias)
    data ={"lista": lista, "success":True}
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")
# Create your views here.


#Agregado adicional al curso
from django.shortcuts import render_to_response
from datetime import datetime
from django.http import HttpResponse
from app.models import *

def home(request):
	return HttpResponse("Hola mundo en holaaa")

def hola(request):
	prueba = "<html><body style='color:red;'>hola</body></html>"
	return HttpResponse(prueba)

def numero(request, numerito):
	return HttpResponse("Hola el numero es %s" % numerito)

def plantilla(request):
	hola = "Soy una variable desde atras"
	contenido = "digamos que soy el contenido"
	titulo = "soy el titulo de la pagina"
	response = render_to_response('hola.html',{'result':hola, 'contenido':contenido, 'title':titulo})
	return HttpResponse(response)

def masdatos(request):
	t0 = datetime.now()
	t1 = t0.strftime("%Y/%m/%d")
	minombre = Editorial.objects.all()[0]
	contenido = 'Aqui va el contenido %s y mi nombre es %s' % (t1, minombre)
 	response = render_to_response('pagina.html',{'title':'Hola soy el titulo :D', 'contenido':contenido})
	return HttpResponse(response)
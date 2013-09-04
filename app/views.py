# Create your views here.


#Agregado adicional al curso
from django.shortcuts import render_to_response


from django.http import HttpResponse

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
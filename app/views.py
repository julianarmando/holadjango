# Create your views here.
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hola mundo")

def hola(request):
	return HttpResponse("Hola mundo en holaaa")

def numero(request, numerito):
	return HttpResponse("Hola el numero es %s" % numerito)
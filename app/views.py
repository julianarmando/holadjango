# Create your views here.
from django.http import HttpResponse

def home(request):
	return HttpResponse("Hola mundo ome :D");
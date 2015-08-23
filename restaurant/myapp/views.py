from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebida

def sobre(request):
	html = "<h1>Proyecto Django </h1>"
	return HttpResponse(html)

def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render(request,'bebidas.html',{'bebidas':bebidas})

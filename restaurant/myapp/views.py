from django.shortcuts import render
from django.http import HttpResponse
from .models import Bebida, Receta

def sobre(request):
	html = "<h1>Proyecto Django </h1>"
	return HttpResponse(html)

def lista_bebidas(request):
	bebidas = Bebida.objects.all()
	return render(request,'bebidas.html',{'bebidas':bebidas})

def inicio(request):
	recetas = Receta.objects.all()
	total = recetas.count()
	return render(request, 'recetas/inicio.html',{'recetas':recetas, 'total':total})
from django.shortcuts import render, get_object_or_404
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

def lista_recetas(request):
	recetas = Receta.objects.all()
	return render(request, 'recetas/recetas.html',{'recetas':recetas})

def detalle_receta(request, id_receta):
	receta = get_object_or_404(Receta, id=id_receta)
	return render(request, 'recetas/receta.html', {'receta':receta})

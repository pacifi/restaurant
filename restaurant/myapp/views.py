from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Bebida, Receta
from .forms import RecetaForm

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

def nueva_receta(request):
    if request.method=='POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/recetas')
    else:
        formulario = RecetaForm()
    return render(request,'recetario/recetaform.html',
                              {'formulario':formulario})


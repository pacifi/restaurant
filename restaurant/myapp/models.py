from django.db import models
from django.contrib.auth.models import User


class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()
	votos = models.IntegerField(default=0)

	def __unicode__(self):
		return self.nombre

class Receta(models.Model):
	titulo = models.CharField(max_length=50,unique=True)
	ingredientes = models.TextField()
	preparacion = models.TextField()
	imagen = models.ImageField(upload_to="recetas")	
	usuario = models.ForeignKey(User)
	tiempo_registro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.titulo	
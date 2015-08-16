from django.db import models

class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()
	votos = models.IntegerField(default=0)

	def __unicode__(self):
		return self.nombre


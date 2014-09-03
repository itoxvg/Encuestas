from django.db import models

# Create your models here.
class Encuesta(models.Model):
	pregunta = models.CharField(max_length=200)
	fecha_pub = models.DateTimeField('fecha de publicacion')

	def __unicode__(self):
		return self.pregunta

class Eleccion(models.Model):
	encuensta = models.ForeignKey(Encuesta)
	texto = models.CharField(max_length=200)
	votos = models.IntegerField()

	def __unicode__(self):
		return self.texto
	
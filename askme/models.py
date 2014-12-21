from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
	titulo = models.CharField(max_length=150)

	def __str__(self):
		return self.titulo

class Pregunta(models.Model):
	asunto = models.CharField(max_length=150)
	descripcion = models.TextField()
	fecha_pub = models.DateTimeField(auto_now_add=True)
	popularidad = models.IntegerField(default=0)
	respuestas = models.IntegerField(default=0)
	categoria = models.ForeignKey(Categoria)
	usuario = models.ForeignKey(User)

	def __str__(self):
		return self.asunto

class Respuesta(models.Model):
	pregunta = models.ForeignKey(Pregunta)
	contenido = models.TextField()
	respuesta_fecha_pub = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(User)
	votos = models.IntegerField(default=0)

	def __str__(self):
		return self.contenido

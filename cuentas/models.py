from django.db import models
from django.contrib.auth.models import User

class DatosUsuario(models.Model):
	usuario = models.OneToOneField(User)
	reputacion = models.IntegerField(default=0)

	def __str__(self):
		return '{0}' .format(self.reputacion)
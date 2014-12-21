from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Categoria, Pregunta, Respuesta
from django.contrib.auth.models import User

# Create your tests here.

class PreguntaTest(TestCase):
	def setUp(self):
		self.categoria = Categoria.objects.create(titulo='novedades')
		self.usuario = User.objects.create_user(username='naffer', password='wizard97')

	def test_es_popular(self):
		test_pregunta = Pregunta.objects.create(
			asunto='prueba', descripcion='texto de prueba',
			usuario=self.usuario, categoria=self.categoria)

		# verificar los valores que deberia tener un objeto recien creado

		self.assertEqual(test_pregunta.respuestas, 0)
		self.assertEqual(test_pregunta.popularidad, 0)
		self.assertEqual(test_pregunta.usuario, self.usuario)
		self.assertEqual(test_pregunta.categoria, self.categoria)

	def test_vistas(self):

		# verificar que la respuesta sea la correcta
		res = self.client.get(reverse('preguntas:preguntas'))
		self.assertEqual(res.status_code, 200)

		self.client.login(username='naffer', password='wizard97')
		res = self.client.get(reverse('preguntas:preguntame'))
		self.assertEqual(res.status_code, 200)

	def test_add(self):
		# verificar que el usuario pueda crear una pregunta correctamente
		self.assertEqual(Pregunta.objects.count(), 0)
		data = {}
		data['asunto'] = 'asunto prueba'
		data['descripcion'] = 'texto de prueba'
		data['categoria'] = self.categoria.id
		self.client.login(username='naffer', password='wizard97')
		res = self.client.post(reverse('preguntas:preguntame'), data)
		self.assertEqual(res.status_code, 302)
		self.assertEqual(Pregunta.objects.count(), 1)
		pregunta = Pregunta.objects.all()[0]
		self.assertEqual(pregunta.asunto, data['asunto'])
		self.assertEqual(pregunta.descripcion, data['descripcion'])
		self.assertEqual(pregunta.categoria, self.categoria)

		# verificar que se pueda crear una respuesta 
		# emular otro usuario que va a responder
		self.assertEqual(pregunta.respuesta_set.count(), 0)
		self.usuario = User.objects.create_user(username='naffer2', password='wizard97')
		self.client.login(username='naffer2', password='wizard97')
		data2 = {}
		data2['contenido'] = 'contenido de prueba'
		res2 = self.client.post(
			reverse('preguntas:detalle', kwargs={'pk': 1}), data2)
		self.assertEqual(res2.status_code, 302)
		self.assertEqual(Respuesta.objects.count(), 1)
		self.assertEqual(pregunta.respuesta_set.count(), 1)
		respuesta = pregunta.respuesta_set.all()[0]
		self.assertEqual(respuesta.contenido, data2['contenido'])
		self.assertEqual(respuesta.usuario, self.usuario)

		# verificar las votaciones en la respuesta
		
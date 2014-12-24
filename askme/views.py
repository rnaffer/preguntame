from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from datetime import datetime

from askme.models import Pregunta, Respuesta, Categoria
from cuentas.models import DatosUsuario
from askme.forms import PreguntarForm, RespuestaForm
# Create your views here.

class PreguntaListView(ListView):
	context_object_name = 'lista_de_preguntas'
	template_name = 'lista_preguntas.html'
	paginate_by = 15

	def get_queryset(self):
		#queryset = [{'popular': Pregunta.objects.order_by('-popularidad'),
		#			'nuevo': Pregunta.objects.order_by('-fecha_pub')}]
		return Pregunta.objects.order_by('-popularidad')

class PreguntaDetailView(FormMixin, DetailView):
	model = Pregunta
	template_name = "detalle.html"
	form_class = RespuestaForm

	def get_queryset(self):
		return Pregunta.objects.all()

	def get_context_data(self, **kwargs):
		context = super(PreguntaDetailView, self).get_context_data(**kwargs)
		context['form'] = RespuestaForm()
		return context

	def post(self, request, *args, **kwargs):
		form = self.get_form(RespuestaForm)
		if form.is_valid():
			respuesta = form.save(commit=False)
			pregunta = self.model.objects.get(pk=self.kwargs['pk'])
			respuesta.usuario = self.request.user
			respuesta.pregunta = pregunta
			respuesta.save()
			pregunta.respuestas += 1
			pregunta.popularidad += 4
			pregunta.save()
			return redirect('/preguntas/{0}' .format(pregunta.id))
		else:
			form = RespuestaForm()
		return render(self.request, self.template_name, self.locals())

class PreguntameFormView(FormView):
	template_name = 'preguntar.html'
	form_class = PreguntarForm
	success_url = '/preguntas'

	def form_valid(self, form):
		pregunta = form.save(commit=False)
		pregunta.usuario = self.request.user
		pregunta.save()
		return super(PreguntameFormView, self).form_valid(form)

def plus(request, respuesta_id):
	respuesta = get_object_or_404(Respuesta, pk=respuesta_id)
	respuesta.votos += 1
	usuario = get_object_or_404(User, username=respuesta.usuario.username)
	datos = DatosUsuario.objects.get(usuario=usuario)
	datos.reputacion += 7
	datos.save()
	respuesta.save()
	return redirect('/preguntas/{0}' .format(respuesta.pregunta.id))

def minus(request, respuesta_id):
	respuesta = get_object_or_404(Respuesta, pk=respuesta_id)
	respuesta.votos -= 1
	respuesta.save()
	return redirect('/preguntas/{0}' .format(respuesta.pregunta.id))

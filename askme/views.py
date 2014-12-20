from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import Context, RequestContext
from django.views.generic import ListView, DetailView
from datetime import datetime

from askme.models import Pregunta, Respuesta, Categoria 
# Create your views here.

class PreguntaListView(ListView):
    context_object_name = 'lista_de_preguntas'
    template_name = 'lista_preguntas.html'

    def get_queryset(self):
    	return Pregunta.objects.order_by('-fecha_pub')

class PreguntaDetailView(DetailView):
	model = Pregunta
	template_name = "detalle.html"

	def get_queryset(self):
		return Pregunta.objects.all()
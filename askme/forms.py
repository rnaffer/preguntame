from django import forms

from askme.models import Categoria, Pregunta, Respuesta

class PreguntarForm(forms.ModelForm):
	class Meta:
		model = Pregunta
		fields = ('asunto', 'descripcion', 'categoria')

class RespuestaForm(forms.ModelForm):
	class Meta:
		model = Respuesta
		fields = ('contenido',)

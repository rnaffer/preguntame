from __future__ import absolute_import

from django.core.exceptions import ValidationError
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

from .models import Answer, Ask

class AnswerForm(forms.ModelForm):
	class Meta:
		fields = ('content',)
		model = Answer

	def __init__(self, *args, **kwargs):
		super(AnswerForm, self).__init__(*args, **kwargs)
		self.fields['content'].label = 'Respuesta'
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'content',
			ButtonHolder(
				Submit('responder', 'Responder', css_class="btn-primary")
			)
		)

class AskForm(forms.ModelForm):
	class Meta:
		fields = ('issue', 'description', 'category')
		model = Ask
		labels = {
			'issue': 'Pregunta',
			'description': 'Descripcion',
			'category': 'Categoria',
		}

	def __init__(self, *args, **kwargs):
		super(AskForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'issue', 
			'description',
			'category',
			ButtonHolder(
				Submit('preguntar', 'Preguntar', css_class="btn-primary")
			)
		)

	def clean_issue(self):
		issue = self.cleaned_data.get('issue')
		try:
		 	Ask.objects.get(issue=issue)
		except Ask.DoesNotExist:
			return issue
		else:
			raise ValidationError('Esta pregunta ya existe')
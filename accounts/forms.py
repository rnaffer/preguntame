from django.contrib.auth.forms import(
	UserCreationForm, AuthenticationForm)

from django import forms
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'email',
			'password1',
			'password2',
			ButtonHolder(
				Submit('registrar', 'Registrar', css_class="btn-primary")
			)
		)

		def save(self, commit=True):
			user = super(UserCreationForm, self).save(commit=False)
			user.email = self.cleaned_data['email']
			if commit:
				user.save()
			return user

class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'username',
			'password',
			ButtonHolder(
				Submit('acceder', 'Acceder', css_class="btn-primary")			
			)
		)
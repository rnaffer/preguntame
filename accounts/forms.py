from django.contrib.auth.forms import(
	UserCreationForm, AuthenticationForm)

from django import forms
from django.contrib.auth.models import User
from .models import UserDetail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(label='Nombre')
	last_name = forms.CharField(label='Apellidos')

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.layout = Layout(
			'first_name',
			'last_name',
			'username',
			'email',
			'password1',
			'password2',
			ButtonHolder(
				Submit('registrar', 'Registrar', css_class="btn-primary verde")
			)
		)

		def save(self, commit=True):
			user = super(UserCreationForm, self).save(commit=False)
			user.email = self.cleaned_data['email']
			user.first_name = self.cleaned_data['first_name']
			user.last_name = self.cleaned_data['last_name']
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
				Submit('acceder', 'Acceder', css_class="btn-primary verde")			
			)
		)

class UserDetailForm(forms.ModelForm):
	class Meta:
		fields = ('profile_image', 'email', 'first_name', 'last_name', 'about_me')
		model = UserDetail
		labels = {
			'profile_image': 'Imagen de perfil', 
			'email': 'Correo electronico',
			'first_name': 'Nombre',
			'last_name': 'Apellidos',
			'about_me': 'Acerca de ti'}

	def __init__(self, *args, **kwargs):
		super(UserDetailForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			'profile_image',
			'email',
			'first_name',
			'last_name',
			'about_me',
			ButtonHolder(
				Submit('guardar', 'Guardar', css_class='btn-primary verde')
			)
		)
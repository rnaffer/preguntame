from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required=True)
	nombre = forms.CharField(max_length=20)
	apellido = forms.CharField(max_length=20)

	class Meta:
		model = User
		fields = ('username', 'nombre', 'apellido', 'email', 'password1', 'password2')

	def save(self, commit):
		user = super(UserCreateForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['nombre']
		user.last_name = self.cleaned_data['apellido']

		if commit:
			user.save()

		return user
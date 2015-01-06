from __future__ import absolute_import

from django.contrib.auth import login, logout, authenticate
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from braces import views

from .models import UserDetail
from .forms import LoginForm, RegistrationForm

class SignUpView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.CreateView
	):
	form_class = RegistrationForm
	form_valid_message = 'Gracias por registrarte, ahora puedes acceder'
	model = User
	success_url = reverse_lazy('accounts:login')
	template_name = 'accounts/signup.html'

	def form_valid(self, form):
		resp = super(SignUpView, self).form_valid(form)
		UserDetail.objects.create(user=self.object)
		return resp

class LogInView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.FormView
	):
	form_class = LoginForm
	form_valid_message = 'Has accedido correctamente'
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LogInView, self).form_valid(form)
		else:
			return self.form_invalid(form)

class LogOutView(
	views.LoginRequiredMixin,
	views.MessageMixin,
	generic.RedirectView
	):
	url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		logout(request)
		self.messages.success('Has salido correctamente')
		return super(LogOutView, self).get(request, *args, **kwargs)
		
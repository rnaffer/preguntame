from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, CreateView
from django.contrib.auth.forms import (
AuthenticationForm, SetPasswordForm, PasswordChangeForm)
from django.contrib import messages

from .forms import UserCreateForm

class LoginFormView(FormView):
	template_name = "log_in.html"
	form_class = AuthenticationForm
	success_url = '/cuentas/login'

	def form_valid(self, form):
		user = form.get_user()
		login(self.request, user)
		return super(LoginFormView, self).form_valid(form)

	def form_invalid(self, form):
		messages.add_message(self.request, messages.ERROR,
			'Usuario o Contraseña Invalido. Por Favor Intente Nuevamente')
		return super(LoginFormView, self).form_invalid(form)
		
class AccountRegistrationView(CreateView):
    template_name = "register.html"
    form_class = UserCreateForm
    success_url = '/cuentas/login'

    def get_success_url(self):
    	if 'next' in self.request.GET:
    		return self.request.GET.get('next')

    	return self.success_url

    def form_valid(self, form):
    	saved_user = form.save(self.request.POST)
    	user = authenticate(
    		username=saved_user.username,
    		password=form.cleaned_data['password1'])
    	login(self.request, user)
    	return HttpResponseRedirect(self.get_success_url())

def logout_view(request):
		logout(request)
		return redirect('/preguntas')
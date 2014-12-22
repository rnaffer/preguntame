from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, render
from cuentas.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView

class LoginFormView(FormView):
	template_name = "log_in.html"
	form_class = LoginForm
	success_url = '/cuentas/login'

	def form_valid(self, form):
		message = None
		username = self.request.POST['username']
		password = self.request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(self.request, user)
				message = 'Te has logueado satisfactoriamente'
			else:
				message = "Tu usuario esta inactivo"
		else:
			message = "Nombre de usuario y/o password incorrectos!"
		return render(self.request, self.template_name, {'form': form, 'message': message})

def logout_view(request):
		logout(request)
		return redirect('/preguntas')
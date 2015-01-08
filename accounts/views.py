from __future__ import absolute_import

from django.contrib.auth import login, logout, authenticate
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from braces import views

from .models import UserDetail
from .forms import LoginForm, RegistrationForm, UserDetailForm

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
		UserDetail.objects.create(
			user=self.object,
			first_name=self.object.first_name,
			last_name=self.object.last_name,
			email=self.object.email
			)
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

class ProfileView(generic.DetailView):
	model = UserDetail
	template_name = 'accounts/profile_detail.html'

	def get_detail(self, pk):
		try:
			user = self.model.objects.get(
				pk=pk
			)
		except UserDetail.DoesNotExist:
			raise Http404
		else:
			return user

	def get(self, request, *args, **kwargs):
		self.object = self.get_detail(kwargs['pk'])
		return super(ProfileView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data(**kwargs)
		# add news and popular asks for sidebar
		context['profile_user'] = User.objects.get(username=self.kwargs['username'])
		return context

class ProfileUpdateView(
	views.LoginRequiredMixin,
	generic.UpdateView
	):
	form_class = UserDetailForm
	model = UserDetail
	template_name = 'accounts/user_update.html'

	def get(self, request, *args, **kwargs):
		self.object = UserDetail.objects.get(user=self.request.user)
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		context = self.get_context_data(object=self.object, form=form)
		return self.render_to_response(self.get_context_data(form=form))
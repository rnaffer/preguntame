from __future__ import absolute_import

from django.contrib import messages 
from django.views import generic
from django.shortcuts import redirect
from django.http import Http404
from django.db.models import Count

from accounts.models import UserDetail
from .models import Answer, Category, Ask
from .forms import AnswerForm, AskForm

from braces import views

class AskSortedMixin(object):
	def get_context_data(self, **kwargs):
		context = super(AskSortedMixin, self).get_context_data(**kwargs)
		# add news and popular asks for sidebar
		context['news_list'] = Ask.objects.news()[:5]
		context['popular_list'] = Ask.objects.popular()[:5]
		return context

class AskListView(
	AskSortedMixin,
	generic.ListView
	):
	model = Ask 

	def get_queryset(self):
		queryset = super(AskListView, self).get_queryset()
		# the annotate avoid make a query in each view
		if 'order' in self.request.GET:
			order = self.request.GET.get('order')
			if order == 'news':
				queryset = Ask.objects.all().order_by('-pub_date')
			elif order == 'popularity':
				queryset = Ask.objects.all().order_by('-popularity')
		
		queryset = queryset.annotate(answer_count=Count('answers'))
		return queryset

class CategoryView(
	AskSortedMixin,
	generic.ListView
	):
	model = Ask
	template_name = 'askme/ask_list.html'

	def get_context_data(self, **kwargs):
		context = super(CategoryView, self).get_context_data(**kwargs)
		# add the category to the context for show the user selection
		category = self.get_category()
		context['category'] = category
		return context

	# get the slug passed as argument in the url and fin the category
	def get_category(self):
		slug = self.kwargs.get('slug', None)

		if slug is not None:
			return Category.objects.get(slug=slug)
		else:
			raise AttributeError("Se deben usar etiquetas para las urls")

	def get_queryset(self):
		queryset = super(CategoryView, self).get_queryset()
		queryset = Ask.objects.filter(category=self.get_category()).order_by('-pub_date')
		# add the annotate to the query because it's another view
		queryset = queryset.annotate(answer_count=Count('answers'))
		return queryset

class AskCreateView(
	views.LoginRequiredMixin,
	generic.CreateView
	):
	form_class = AskForm
	model = Ask

	def form_valid(self, form):
		# set the user to the new ask
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		# increase rating of the ask user
		user_detail = UserDetail.objects.get(user=self.request.user)
		user_detail.rating += 2
		user_detail.save()
		return super(AskCreateView, self).form_valid(form)
	
class AskDetailList(
	AskSortedMixin,
	views.PrefetchRelatedMixin,
	generic.DetailView
	):
	form_class = AnswerForm
	model = Ask
	http_method_names = ['get', 'post']
	prefetch_related = ('answers',)

	def get_context_data(self, **kwargs):
		# update the form info
		context = super(AskDetailList, self).get_context_data(**kwargs)
		context.update({'form': self.form_class(self.request.POST or None)})
		# add the ask category to the context
		context['category'] = self.object.category
		context['related_list'] = Ask.objects.related(self.object.category.title)[:5]
		return context

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			# get the ask and set populaity
			obj = self.get_object()
			obj.popularity += 6
			obj.save()
			# increase the rating of the ask user
			ask_user_detail = UserDetail.objects.get(user=obj.user)
			ask_user_detail.rating += 2
			ask_user_detail.save()
			# create the answer and redirect to the ask
			answer = form.save(commit=False)
			answer.user = self.request.user
			answer.ask = obj
			answer.save()
		else:
			return self.get(request, *args, **kwargs)
		return redirect(obj)
		
class VoteUpView(
	views.LoginRequiredMixin,
	generic.RedirectView
	):
	
	def get(self, request, *args, **kwargs):
		# find the answer pk and set vote
		id = self.kwargs['pk']
		answer = Answer.objects.get(pk=id)
		answer.votes += 1
		answer.save()
		# find the answer user and increase rating
		user_detail = UserDetail.objects.get(user=answer.user)
		user_detail.rating += 3
		user_detail.save()
		# increase the ask popularity and redirect to ask
		obj = answer.ask
		obj.popularity += 2
		obj.save()
		return redirect(obj)

class VoteDownView(
	views.LoginRequiredMixin,
	generic.RedirectView
	):
	
	def get(self, request, *args, **kwargs):
		# find the answer pk and remove vote
		id = self.kwargs['pk']
		answer = Answer.objects.get(pk=id)
		answer.votes -= 1
		answer.save()
		# find the answer user and decrease rating
		user_detail = UserDetail.objects.get(user=answer.user)
		user_detail.rating -= 2
		user_detail.save()
		# decrease the ask popularity and redirect to ask
		obj = answer.ask
		obj.popularity -= 1
		obj.save()
		return redirect(obj)
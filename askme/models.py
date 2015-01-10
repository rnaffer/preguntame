from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=50)
	slug = models.SlugField(max_length='255', blank=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		return super(Category, self).save(*args, **kwargs)

class AskQuerySet(models.query.QuerySet):
	def news(self):
		return self.order_by('-pub_date')

	def popular(self):
		return self.order_by('-popularity')

	def related(self, category):
		return self.filter(category__title=category).order_by('-popularity')

class AskManager(models.Manager):
	def news(self):
		return self.get_queryset().news()

	def popular(self):
		return self.get_queryset().popular()

	def related(self, category):
		return self.get_queryset().related(category)

	def get_queryset(self):
		return AskQuerySet(self.model, using=self._db)

class Ask(models.Model):
	user = models.ForeignKey(User, related_name='asks')
	issue = models.CharField(max_length=150)
	description = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	popularity = models.IntegerField(default=0)
	category = models.ForeignKey(Category, related_name='asks')
	slug = models.SlugField(max_length='255', blank=True)

	objects = AskManager()

	class Meta:
		unique_together = ('user', 'issue')

	def __str__(self):
		return self.issue

	def save(self, *args, **kwargs):
		self.slug = slugify(self.issue)
		return super(Ask, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('askme:detail', kwargs={'slug': self.slug})

class Answer(models.Model):
	user = models.ForeignKey(User, related_name='answers')
	ask = models.ForeignKey(Ask, related_name='answers')
	content = models.TextField()
	answer_pub_date = models.DateTimeField(auto_now_add=True)
	votes = models.IntegerField(default=0)
	slug = models.SlugField(max_length='255', blank=True, default='')

	class Meta:
		unique_together = ('ask', 'content')

	def __str__(self):
		return self.content

	def save(self, *args, **kwargs):
		self.slug = slugify(self.ask)
		return super(Answer, self).save(*args, **kwargs)

class AnswerVoteUsers(models.Model):
	answer = models.ForeignKey(Answer, related_name='users')
	username = models.CharField(max_length=150)

from django.db import models

from django.core.urlresolvers import reverse

import os

from django.contrib.auth.models import User

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance.id), filename)

class UserDetail(models.Model):
	user = models.OneToOneField(User, related_name='details', unique=True)
	rating = models.IntegerField(default=1)
	profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
	email = models.EmailField(default="user@email.com")
	first_name = models.CharField(default='user_name', max_length=50)
	last_name = models.CharField(default='user_name', max_length=50)
	about_me = models.TextField(blank=True, null=True)

	class Meta:
		unique_together = ('user', 'rating')

	def __str__(self):
		return '{0} {1}' .format(self.first_name, self.last_name)

	def get_absolute_url(self):
		return reverse('accounts:profile', kwargs={'pk': self.id, 'username': self.user.username})
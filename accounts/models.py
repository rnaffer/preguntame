from django.db import models

from django.contrib.auth.models import User

class UserDetail(models.Model):
	user = models.OneToOneField(User, related_name='details')
	rating = models.IntegerField(default=1)

	class Meta:
		unique_together = ('user', 'rating')

	def __str__(self):
		return self.user.username
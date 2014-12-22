from django.db import models
from django.contrib.auth.models import User, UserManager

class CustomUser(User):
	
	objects = UserManager()
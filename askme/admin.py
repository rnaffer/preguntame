from django.contrib import admin

from .models import Answer, Ask, Category

admin.site.register(Answer)
admin.site.register(Ask)
admin.site.register(Category)

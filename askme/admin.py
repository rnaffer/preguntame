from django.contrib import admin

from askme.models import Categoria, Pregunta, Respuesta
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
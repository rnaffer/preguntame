from django.contrib import admin

from askme.models import Categoria, Pregunta, Respuesta
# Register your models here.

class RespuestaAdmin(admin.ModelAdmin):
	list_display = ('contenido', 'respuesta_fecha_pub', 'votos', 'usuario')
	list_filter = ('respuesta_fecha_pub', 'votos', 'usuario')

class RespuestaInline(admin.StackedInline):
	model = Respuesta
	extra = 5
	raw_id_fields = ('usuario',)

class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('asunto', 'descripcion', 'fecha_pub', 'popularidad', 'respuestas', 
		'categoria', 'usuario')
	list_filter = ('categoria', 'usuario', 'fecha_pub', 'popularidad', 'respuestas')
	raw_id_fields = ('categoria', 'usuario')
	inlines = [RespuestaInline]

class PreguntaInline(admin.StackedInline):
	model = Pregunta
	extra = 3
	raw_id_fields = ('usuario',)

class CategoriaAdmin(admin.ModelAdmin):
	inlines = [PreguntaInline]

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
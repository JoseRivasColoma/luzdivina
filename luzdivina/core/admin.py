from django.contrib import admin
from .models import TipoEvento, Evento, EstadoEvento, TipoPersona, Persona, Comunidad

# Register your models here.

class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class ComunidadAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'ubicacion',)

class EventoAdmin(admin.ModelAdmin):
    list_display = ('fecha_evento', 'hora_evento', 'descripcion', 'direccion','tipo_evento', 'estado_evento')
    search_fields = ['tipo_evento', 'estado_evento']
    list_filter = ('tipo_evento', 'estado_evento')

class EstadoEventoAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class TipoPersonaAdmin(admin.ModelAdmin):
    list_display = ('descripcion',)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'sexo', 'edad', 'direccion', 'tipo_persona')
    search_fields = ['nombre', 'tipo_persona']
    list_filter = ('nombre', 'tipo_persona')

admin.site.register(TipoEvento, TipoEventoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(EstadoEvento, EstadoEventoAdmin)
admin.site.register(TipoPersona, TipoPersonaAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Comunidad, ComunidadAdmin)
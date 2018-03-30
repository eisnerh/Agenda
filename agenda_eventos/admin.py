# Register your models here.
from django.contrib import admin
from agenda_eventos.models import *

admin.site.register(Material)
admin.site.register(Evento)
admin.site.register(ClasificacionEvento)
admin.site.register(Cliente)
admin.site.register(DetalleEvento)
admin.site.register(EventoCliente)
admin.site.register(EventoMaterial)

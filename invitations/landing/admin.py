from django.contrib import admin
from .models import Participante, Asistente

# Register your models here.
class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    ordering = ('orden_compra', 'nombre')
    list_display = ('codigo_participante', 'nombre', 'telefono', 'email', 'empresa', 'giro', 'cargo', 'orden_compra', 'f_name', 'nit', 'nrc')

class AsistenteAdmin(admin.ModelAdmin):
    readonly_fields = ('participante', 'registered_at',)
    list_display = ('participante', 'registered_at')

admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Asistente, AsistenteAdmin)

from django.contrib import admin
from .models import Participante, Asistente

# Register your models here.
class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class AsistenteAdmin(admin.ModelAdmin):
    readonly_fields = ('participante', 'registered_at',)

admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Asistente, AsistenteAdmin)

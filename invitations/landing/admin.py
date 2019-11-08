from django.contrib import admin
from .models import Participante

# Register your models here.
class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

admin.site.register(Participante, ParticipanteAdmin)

from django.db import models

# Create your models here.
class Participante(models.Model):

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
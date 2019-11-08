from django.db import models

# Create your models here.
class Participante(models.Model):
    codigo_participante = models.CharField(max_length=255, unique=True, verbose_name="Código de participante")
    nombre = models.CharField(max_length=255, verbose_name="Nombre del participante")
    empresa = models.CharField(max_length=255, verbose_name="Empresa (Razón social)")
    cargo = models.CharField(max_length=100, verbose_name="Cargo")
    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Número de teléfono", blank=True, null=True)
    f_name = models.CharField(max_length=255, verbose_name="Facturar a nombre de")
    nit = models.CharField(max_length=17, verbose_name="NIT")
    nrc = models.CharField(max_length=10, verbose_name="NRC")
    orden_compra = models.CharField(max_length=255, verbose_name="Orden de compra No.", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
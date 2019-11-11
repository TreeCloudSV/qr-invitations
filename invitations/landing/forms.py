from django import forms
from .models import Participante


class RegistrarForm(forms.ModelForm):

    class Meta:
        model = Participante
        fields = ['nombre', 'empresa', 'cargo', 'email', 'telefono',
                  'f_name', 'direccion', 'giro', 'nit', 'nrc', 'orden_compra']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Participante.objects.filter(email=email).exists():
            raise forms.ValidationError("El email que ingresó ya está registrado")
        return email

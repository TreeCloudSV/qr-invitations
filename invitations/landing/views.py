from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms
from django.core.mail import send_mail

from landing.models import Participante, Asistente
from .forms import RegistrarForm

class RegisterView(CreateView):
    model = Participante
    form = RegistrarForm
    template_name = 'landing/index.html'
    fields = ['nombre', 'empresa', 'cargo', 'email', 'telefono',
              'f_name', 'nit', 'nrc', 'orden_compra']

    def get_form(self, form_class=None):
        form = super(RegisterView, self).get_form()
        form.fields['nombre'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su nombre", 'class': "form-control-mod"})
        form.fields['empresa'].widget = forms.TextInput(attrs={'placeholder': "Ingrese empresa o razón social", 'class': "form-control-mod"})
        form.fields['cargo'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su cargo", 'class': "form-control-mod"})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder': "Ingrese su email", 'class': "form-control-mod"})
        form.fields['telefono'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su número de teléfono", 'class': "form-control-mod"})
        form.fields['f_name'].widget = forms.TextInput(attrs={'placeholder': "A nombre de quien se facturará", 'class': "form-control-mod"})
        form.fields['nit'].widget = forms.TextInput(attrs={'placeholder': "Número de NIT", 'class': "form-control-mod"})
        form.fields['nrc'].widget = forms.TextInput(attrs={'placeholder': "Número de NRC", 'class': "form-control-mod"})
        form.fields['orden_compra'].widget = forms.TextInput(attrs={'placeholder': "Orden de compra", 'class': "form-control-mod"})
        return form


def finish(request, codigo):
    participante = get_object_or_404(Participante, codigo_participante=codigo)
    return render(request, 'landing/finish.html', {
        'participante': participante
    })


@staff_member_required
def validate(request, codigo_participante):
    asistente = None
    errors = None
    try:
        participante = Participante.objects.get(codigo_participante__exact = codigo_participante)
        asistente = Asistente.objects.get(participante__exact = participante)

    except Participante.DoesNotExist as e:
        errors = 'Participante no ha se encuentra registrado'
    except Asistente.DoesNotExist as e:
        asistente = Asistente.objects.create(participante=participante)

    context = {
        'asistente': asistente,
        'errors': errors
    }
    
    return render(request, 'landing/validate.html',context)
import os
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import get_template
from django import forms
from django.core.mail import send_mail
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from landing.models import Participante, Asistente
from .forms import RegistrarForm


class RegisterView(CreateView):
    model = Participante
    form = RegistrarForm
    fields = ['nombre', 'empresa', 'cargo', 'email', 'telefono',
              'f_name', 'direccion', 'giro', 'nit', 'nrc', 'orden_compra']

    def get_form(self, form_class=None):
        form = super(RegisterView, self).get_form()
        form.fields['captcha'] = ReCaptchaField(
            required=True,
            widget=ReCaptchaV2Checkbox())
        form.fields['nombre'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su nombre", 'class': "form-control-mod"})
        form.fields['empresa'].widget = forms.TextInput(attrs={'placeholder': "Ingrese empresa o razón social", 'class': "form-control-mod"})
        form.fields['cargo'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su cargo", 'class': "form-control-mod"})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder': "Ingrese su email", 'class': "form-control-mod"})
        form.fields['telefono'].widget = forms.TextInput(attrs={'placeholder': "Ingrese su número de teléfono", 'class': "form-control-mod"})
        form.fields['f_name'].widget = forms.TextInput(attrs={'placeholder': "A nombre de quien se facturará", 'class': "form-control-mod"})
        form.fields['direccion'].widget = forms.TextInput(attrs={'placeholder': "Dirección", 'class': "form-control-mod"})
        form.fields['giro'].widget = forms.TextInput(attrs={'placeholder': "Giro de la empresa", 'class': "form-control-mod"})
        form.fields['nit'].widget = forms.TextInput(attrs={'placeholder': "Número de NIT", 'class': "form-control-mod"})
        form.fields['nrc'].widget = forms.TextInput(attrs={'placeholder': "Número de NRC", 'class': "form-control-mod"})
        form.fields['orden_compra'].widget = forms.TextInput(attrs={'placeholder': "Orden de compra", 'class': "form-control-mod"})

        return form

    def form_valid(self, form):
        participante = form.save(commit=False)
        recipient_list = [participante.email]
        msg_plain = '¡Gracias por registrarse! Puedes acceder a tu registro a través de este enlace:'
        msg_html = get_template('landing/mail.html')
        send_mail(
            'BCC El Salvador',
            msg_plain,
            os.getenv("EMAIL_HOST_USER"),
            recipient_list,
            html_message=msg_html.render({'participante': participante}),
        )
        form.save()
        return super(RegisterView, self).form_valid(form)


def finish(request, codigo):
    try:
        participante = Participante.objects.get(codigo_participante=codigo)
        return render(request, 'landing/finish.html', {
            'participante': participante
        })
    except:
        return redirect('index')


def validate(request, codigo_participante):
    asistente = None
    errors = None
    try:
        participante = Participante.objects.get(codigo_participante=codigo_participante)
        asistente, created = Asistente.objects.get_or_create(participante=participante)
    except Participante.DoesNotExist as e:
        errors = 'Participante no ha se encuentra registrado'
    # Context data
    context = {
        'nombre': asistente,
        'errors': errors
    }
    return render(request, 'landing/validate.html',context)

def prueba(request):
    participante = Participante.objects.get(codigo_participante='09c76072be')
    return render(request, 'landing/mail.html', {'participante': participante})
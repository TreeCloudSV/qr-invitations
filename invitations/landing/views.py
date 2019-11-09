from django.shortcuts import render
from landing.models import Participante, Asistente
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    context = {
        'data': Participante.objects.all()[0].codigo_participante
    }
    
    return render(request, 'landing/index.html',context)


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


from django.shortcuts import render, get_object_or_404
from .models import Participante,Evento
# Create your views here.

def lista_participantes(request):
    participantes = Participante.objects.all().order_by('nombre_participante')

    contexto = {
        'participantes': participantes
    }

    return render(request,'constancias/lista_participantes.html',contexto)


def detalle_participante(request,pk):
    participante = get_object_or_404(participante,id_participante = pk)

    evento_registrado = participante.evento_id

    contexto = {
        'participante':participante,
        'evento': evento_registrado,
    }

    return render(request,'constancias/detalle_participante.html',contexto)


def lista_eventos(request):
    eventos = Evento.objects.all().order_by('titulo_evento')

    contexto = {
        'eventos': eventos
    }

    return render(request,'constancias/lista_eventos.html',contexto)


from django.shortcuts import render, get_object_or_404
from .models import Participante,Evento
from django.db.models import Min
# Create your views here.

def lista_participantes(request):
    

    ids_unicos = Participante.objects.values('email_participante').annotate(
        min_id=Min('id_participante')
    ).values_list('min_id', flat=True) 
    
    
    participantes = Participante.objects.filter(id_participante__in=ids_unicos).order_by('email_participante')
    
    
    
    contexto = {
        'participantes': participantes
    }
    
    return render(request, 'constancias/lista_participantes.html', contexto)


# constancias/views.py

def detalle_participante(request, pk):
    # 1. Asigna 'participante' de manera segura
    participante = get_object_or_404(Participante, id_participante=pk)
    
    # 2. Accede a los eventos a través del related_name 'eventos'
    eventos_registrados = participante.eventos.all() 
    
    contexto = {
        'participante': participante,
        'eventos': eventos_registrados, 
    }
    
    return render(request, 'constancias/detalle_participante.html', contexto)

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('titulo_evento')

    contexto = {
        'eventos': eventos
    }

    return render(request,'constancias/lista_eventos.html',contexto)

def detalle_evento(request,pk):
    
    evento = get_object_or_404(Evento,id_evento=pk)

    participantes_evento = evento.participantes.all().order_by('nombre_participante')

    contexto = {
        'evento': evento,
        'participantes': participantes_evento
    }

    return render(request, 'constancias/detalle_evento.html', contexto)

    


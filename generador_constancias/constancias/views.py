from django.shortcuts import render,redirect ,get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import GenerarConstanciaForm
from docx import Document 
from io import BytesIO 
import os
from django.conf import settings
from .models import Participante, Evento, Plantilla
from django.db.models import Min

# Create your views here.

@login_required
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

@login_required
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

@login_required
def lista_eventos(request):
    eventos = Evento.objects.all().order_by('titulo_evento')

    contexto = {
        'eventos': eventos
    }

    return render(request,'constancias/lista_eventos.html',contexto)

@login_required
def detalle_evento(request,pk):
    
    evento = get_object_or_404(Evento,id_evento=pk)

    participantes_evento = evento.participantes.all().order_by('nombre_participante')

    contexto = {
        'evento': evento,
        'participantes': participantes_evento
    }

    return render(request, 'constancias/detalle_evento.html', contexto)

    

@login_required
def generar_constancia(request, participante_pk, evento_pk, plantilla_pk):
    # 1. OBTENER OBJETOS
    try:
        # Usa _pk en la función y en el filtro de la base de datos
        evento = Evento.objects.get(id_evento=evento_pk)
        participante = Participante.objects.get(id_participante=participante_pk)
        plantilla = Plantilla.objects.get(id_plantilla=plantilla_pk) 
        
    except (Evento.DoesNotExist, Participante.DoesNotExist, Plantilla.DoesNotExist) as e:
        # Manejo de error si no se encuentran los objetos
        return HttpResponse("Error: Objeto no encontrado. Detalle: " + str(e), status=404)

    # 2. DEFINIR SUSTITUCIONES
    sustituciones = {
        # ¡IMPORTANTE! Mantén la convención de doble llave
        '{{TITULO_EVENTO}}': evento.titulo_evento,
        '{{NOMBRE_PARTICIPANTE}}': participante.nombre_participante,
        '{{ROL_PARTICIPANTE}}': participante.rol_participante,        
        '{{FECHA_INICIO}}': evento.fecha_inicio.strftime('%d/%m/%Y'),
        '{{FECHA_FIN}}': evento.fecha_fin.strftime('%d/%m/%Y'),
    }

    # 3. CARGAR EL DOCUMENTO
    try:
        # Carga el archivo .docx desde la ruta del FileField
        document = Document(plantilla.archivo.path)
    except Exception as e:
        return HttpResponse(f"Error al cargar el archivo DOCX: {e}", status=500)


    # 4. LÓGICA DE REEMPLAZO (Función central para sustituir texto)
    def replace_text_in_element(element, replacements):
        """Reemplaza los marcadores en un párrafo o celda."""
        # Se itera sobre los runs porque si el texto tiene formato,
        # python-docx lo divide.
        for run in element.runs:
            for key, value in replacements.items():
                if key in run.text:
                    run.text = run.text.replace(key, value)

    def replace_all_markers(doc, replacements):
        # A. Reemplazar en párrafos (cuerpo principal)
        for p in doc.paragraphs:
            replace_text_in_element(p, replacements)
        
        # B. Reemplazar en tablas (muy común en plantillas complejas)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        replace_text_in_element(p, replacements)

    replace_all_markers(document, sustituciones)


    # 5. PREPARAR RESPUESTA HTTP
    
    # Prepara el nombre del archivo para la descarga
    nombre_archivo = f"Constancia_{participante.nombre_participante.replace(' ', '_')}.docx"
    
    # Crea el objeto de respuesta HTTP para un archivo DOCX
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo}"'
    
    # Guarda el documento modificado directamente en la respuesta
    document.save(response)

    return response
    
   


@login_required
def pagina_generar_constancia(request):
    if request.method == 'POST':
        form = GenerarConstanciaForm(request.POST)
        
        if form.is_valid():            
            participante_id = form.cleaned_data['participante'].id_participante
            evento_id = form.cleaned_data['evento'].id_evento
            plantilla_obj = form.cleaned_data['plantilla']           
            
            return redirect(reverse('generar_constancia', args=[participante_id, evento_id, plantilla_obj.id_plantilla]))
    else:
        
        form = GenerarConstanciaForm()

    contexto = {'form': form}
    return render(request, 'constancias/pagina_generar.html', contexto)
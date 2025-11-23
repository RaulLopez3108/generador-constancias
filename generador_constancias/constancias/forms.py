# constancias/forms.py

from django import forms
from .models import Participante, Evento, Plantilla

class GenerarConstanciaForm(forms.Form):
    
        
    participante = forms.ModelChoiceField(
        queryset=Participante.objects.all().order_by('nombre_participante'),
        label="Seleccionar Participante"
    )
    
    evento = forms.ModelChoiceField(
        queryset=Evento.objects.all().order_by('-fecha_inicio'), 
        label="Seleccionar Evento"
    )
    
    
    plantilla = forms.ModelChoiceField(
        queryset=Plantilla.objects.filter(activa=True).order_by('nombre_plantilla'),
        label="Seleccionar Plantilla"
    )



class CargaParticipantesForm(forms.Form):
    archivo_csv = forms.FileField(
        label='Archivo CSV'
    )
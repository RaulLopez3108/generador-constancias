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


class EventoForm(forms.ModelForm):
    # Campo personalizado para subir archivo de plantilla
    archivo_plantilla = forms.FileField(
        label="Plantilla de Constancia",
        help_text="Suba un archivo .docx para usar como plantilla de constancia",
        required=False,  # No obligatorio para permitir editar eventos sin cambiar plantilla
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.docx,.doc'
        })
    )
    
    class Meta:
        model = Evento
        fields = ['titulo_evento', 'tipo_evento', 'modalidad_evento', 'fecha_inicio', 
                 'fecha_fin', 'duracion_horas', 'descripcion', 'participantes']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalizar widgets y atributos
        self.fields['titulo_evento'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ej: Conferencia Internacional de Tecnología 2025'
        })
        
        self.fields['tipo_evento'].widget.attrs.update({
            'class': 'form-control'
        })
        
        self.fields['modalidad_evento'].widget.attrs.update({
            'class': 'form-control'
        })
        
        # Formato de fecha dd/mm/yyyy
        self.fields['fecha_inicio'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['fecha_inicio'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']
        
        self.fields['fecha_fin'].widget = forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
        self.fields['fecha_fin'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']
        
        self.fields['duracion_horas'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Ej: 40',
            'min': '1',
            'max': '500'
        })
        
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',
            'rows': '4',
            'maxlength': '150',
            'placeholder': 'Breve descripción del evento (máximo 150 caracteres)'
        })
        
        # Campos obligatorios
        self.fields['titulo_evento'].required = True
        self.fields['tipo_evento'].required = True
        self.fields['modalidad_evento'].required = True
        self.fields['fecha_inicio'].required = True
        self.fields['fecha_fin'].required = True
        
        # El archivo de plantilla solo es obligatorio al crear un nuevo evento
        if not self.instance or not self.instance.pk:
            self.fields['archivo_plantilla'].required = True
        else:
            self.fields['archivo_plantilla'].required = False
        
        # Campos opcionales
        self.fields['duracion_horas'].required = False
        self.fields['descripcion'].required = False
        
        # Configurar campo participantes si está presente
        if 'participantes' in self.fields:
            self.fields['participantes'].widget.attrs.update({
                'class': 'form-control',
                'multiple': True,
                'size': '5'
            })
            self.fields['participantes'].required = False

    def clean_archivo_plantilla(self):
        archivo = self.cleaned_data.get('archivo_plantilla')
        
        # Si es un evento nuevo y no hay archivo, es requerido
        if not self.instance or not self.instance.pk:
            if not archivo:
                raise forms.ValidationError("La plantilla es obligatoria para eventos nuevos.")
        
        # Si hay archivo, validarlo
        if archivo:
            if not archivo.name.endswith(('.docx', '.doc')):
                raise forms.ValidationError("El archivo debe ser un documento de Word (.docx o .doc)")
            if archivo.size > 5 * 1024 * 1024:  # 5MB máximo
                raise forms.ValidationError("El archivo no puede ser mayor a 5MB")
        
        return archivo

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        
        if fecha_inicio and fecha_fin:
            if fecha_fin < fecha_inicio:
                raise forms.ValidationError("La fecha de finalización no puede ser anterior a la fecha de inicio.")
        
        return cleaned_data


class CargaParticipantesForm(forms.Form):
    archivo_csv = forms.FileField(
        label='Archivo CSV'
    )


class ParticipanteForm(forms.ModelForm):
    """Formulario para crear/editar participantes individuales"""
    
    ROLES_CHOICES = [
        ('Participante', 'Participante'),
        ('Ponente', 'Ponente'),
        ('Organizador', 'Organizador'),
        ('Facilitador', 'Facilitador'),
    ]
    
    nombre_participante = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre completo del participante',
        }),
        label='Nombre Completo',
        help_text='Nombre completo del participante (mínimo 3 caracteres)'
    )
    
    email_participante = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'correo@ejemplo.com',
        }),
        label='Correo Electrónico',
        help_text='Dirección de correo electrónico única'
    )
    
    rol_participante = forms.ChoiceField(
        choices=ROLES_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
        }),
        label='Rol del Participante',
        help_text='Seleccione el rol que tendrá en los eventos'
    )
    
    class Meta:
        model = Participante
        fields = ['nombre_participante', 'email_participante', 'rol_participante']
        
    def clean_nombre_participante(self):
        nombre = self.cleaned_data.get('nombre_participante')
        if len(nombre.strip()) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return nombre.strip()
    
    def clean_email_participante(self):
        email = self.cleaned_data.get('email_participante')
        if email:
            email = email.lower().strip()
            # Verificar si ya existe (excluyendo la instancia actual en caso de edición)
            existing = Participante.objects.filter(email_participante=email)
            if self.instance and self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)
            
            if existing.exists():
                raise forms.ValidationError("Ya existe un participante con este correo electrónico.")
        return email


class CargaCSVForm(forms.Form):
    """Formulario mejorado para carga masiva por CSV"""
    
    archivo_csv = forms.FileField(
        label='Archivo CSV',
        help_text='Seleccione un archivo CSV con los participantes (máximo 5MB)',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.csv',
        })
    )
    
    evento_id = forms.ModelChoiceField(
        queryset=Evento.objects.all().order_by('-fecha_inicio'),
        required=False,
        empty_label="No asociar a evento específico",
        label='Asociar a Evento',
        help_text='Opcional: Todos los participantes se asociarán automáticamente al evento seleccionado',
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    
    def clean_archivo_csv(self):
        archivo = self.cleaned_data.get('archivo_csv')
        
        if archivo:
            # Validar tamaño (5MB máximo)
            if archivo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("El archivo es demasiado grande. Máximo 5MB permitido.")
            
            # Validar extensión
            if not archivo.name.lower().endswith('.csv'):
                raise forms.ValidationError("Solo se permiten archivos CSV (.csv).")
                
        return archivo
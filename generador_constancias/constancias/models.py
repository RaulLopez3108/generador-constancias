from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)    
    nombre_participante = models.CharField(max_length=100)
    rol_participante = models.CharField(
        max_length=50,
        default="",
        help_text="Rol del participante en el evento")
    email_participante = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_participante
    
    def get_absolute_url(self):
        return reverse('detalle_participante', args=[str(self.id_participante)])

class ModalidadEvento(models.TextChoices):
    PRESENCIAL = "PRE", "Presencial"
    VIRTUAL = "VIR", "Virtual"
    HIBRIDO = "HIB", "Hibrido"


class TipoEvento(models.TextChoices):
    CURSO = "CUR", "Curso"
    TALLER = "TAL", "Taller"
    SEMINARIO = "SEM", "Seminario"
    CONFERENCIA = "CON", "Conferencia"
    DIPLOMADO = "DIP", "Diplomado"
    CONGRESO = "COG", "Congreso"


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    titulo_evento = models.CharField(max_length=100)
    tipo_evento = models.CharField(
        max_length=3,
        choices=TipoEvento.choices,
        default=TipoEvento.CONFERENCIA,
        verbose_name="Tipo de Evento") 
    modalidad_evento = models.CharField(
        max_length=3,
        choices=ModalidadEvento.choices,
        default=ModalidadEvento.PRESENCIAL,
        verbose_name="Modalidad de Evento")
    
    # Fechas del evento
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    # Duracion en horas
    duracion_horas = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(500)],
        help_text="Duración total del evento en horas académicas",
        verbose_name="Duración (horas)",
        null=True,
        blank=True
    )
    
    participantes = models.ManyToManyField(
        'Participante', 
        related_name='eventos',
        blank=True)
    plantilla_id = models.ForeignKey('Plantilla', on_delete=models.CASCADE)
    activo = models.BooleanField()
    descripcion = models.TextField(
        max_length=150,
        blank=True,
        default="",
        verbose_name="Descripción",
        help_text="Descripción del evento")

    def __str__(self):
        return self.titulo_evento
    
    def get_absolute_url(self):
        return reverse('detalle_evento', args=[str(self.id_evento)])
    
class Plantilla(models.Model):
    id_plantilla = models.AutoField(primary_key=True)
    nombre_plantilla = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='plantillas/')
    fecha_creacion = models.DateField()
    activa = models.BooleanField()

    def __str__(self):
        return self.nombre_plantilla



class Constancia(models.Model):
    id_participante = models.ForeignKey('Participante', on_delete=models.CASCADE)
    estado = models.BooleanField()
    archivo = models.FileField(upload_to='constancias/')
    fecha_creacion = models.DateField()



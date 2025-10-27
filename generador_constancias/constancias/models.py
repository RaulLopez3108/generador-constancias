from django.db import models

# Create your models here.
class Participante(models.Model):
    id_participante = models.AutoField(primary_key=True)
    evento_id = models.ForeignKey('Evento', on_delete=models.CASCADE)
    nombre_participante = models.CharField(max_length=100)
    email_participante = models.EmailField()

    def __str__(self):
        return self.nombre_participante
    
    def get_absolute_url(self):
        return reversed('detalle del participante',args=[str(self.id_participante)])

class ModalidadEvento(models.TextChoices):
    PRESENCIAL = "PRE", "Presencial"
    VIRTUAL = "VIR", "Virtual"
    HIBRIDO = "HIB", "Hibrido"


class TipoEVento(models.TextChoices):
    CURSO = "CUR", "Curso"
    TALLER = "TAL", "Taller"
    SEMINARIO = "SEM", "Seminario"
    CONFERENCIA = "CON", "Conferencia"
    DIPLOMADO = "DIP", "Diplomado"
    CONGRESO = "CONG", "Congreso"


class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    titulo_evento = models.CharField(max_length=100)
    tipo_evento = models.CharField(choices=TipoEVento.choices,default=TipoEVento.CONFERENCIA) 
    modalidad_evento = models.CharField(choices=ModalidadEvento.choices,default=ModalidadEvento.PRESENCIAL)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    plantilla_id = models.ForeignKey('Plantilla', on_delete=models.CASCADE)
    activo = models.BooleanField()

    def __str__(self):
        return self.titulo_evento
    
    def get_absolute_url(self):
        return reversed('detalle del evento', args=[str(self.id_evento)])
    
class Plantilla(models.Model):
    id_plantilla = models.AutoField(primary_key=True)
    nombre_plantilla = models.CharField()
    archivo = models.FileField()
    fecha_creacion = models.DateField()
    activa = models.BooleanField()

class Constancia(models.Model):
    id_participante = models.ForeignKey('Participante', on_delete=models.CASCADE)
    estado = models.BooleanField()
    archivo = models.FileField()
    fecha_creacion = models.DateField()



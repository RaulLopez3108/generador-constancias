from django.contrib import admin
from .models import Participante,Evento,Plantilla
from django.db.models import Min # Necesitas importar Min

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre_participante', 'email_participante')
    search_fields = ('nombre_participante', 'email_participante')

    

# Registrar el modelo con la clase modificada
admin.site.register(Participante, ParticipanteAdmin)


admin.site.register(Evento)
admin.site.register(Plantilla)
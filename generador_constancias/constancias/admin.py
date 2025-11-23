import csv
import io
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django.urls import path
from .models import Participante 
from .forms import CargaParticipantesForm 
from django.http import HttpResponseRedirect
from .models import Participante, Evento, Plantilla, Constancia

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre_participante', 'email_participante')
    search_fields = ('nombre_participante', 'email_participante')

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nombre_participante', 'email_participante')
    search_fields = ('nombre_participante', 'email_participante')
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
           
            path('cargar-csv/', self.cargar_csv, name='participante_cargar_csv'),
        ]
        return custom_urls + urls
    def cargar_csv(self, request):
        if request.method == "POST":
            form = CargaParticipantesForm(request.POST, request.FILES)
            if form.is_valid():
                archivo = request.FILES['archivo_csv']                
                
                try:
                    archivo_decodificado = archivo.read().decode('utf-8')
                    datos_io = io.StringIO(archivo_decodificado)
                    lector_csv = csv.reader(datos_io)
                    
                    next(lector_csv)                     
                    contador = 0
                    for fila in lector_csv:
                        nombre = fila[0]
                        email = fila[1]
                        rol = fila[2]
                        
                        Participante.objects.update_or_create(
                            email_participante=email,
                            rol_participante = rol,
                            defaults={'nombre_participante': nombre}
                        )
                        contador += 1                    
                    self.message_user(request, f"¡Carga exitosa! Se procesaron {contador} participantes.")
                    return HttpResponseRedirect("../") 
                
                except Exception as e:
                    self.message_user(request, f"Error en el procesamiento del CSV: {e}", level=messages.ERROR)
                   
                    return HttpResponseRedirect("../cargar-csv/") 
        else:           
            form = CargaParticipantesForm()                
        contexto = self.admin_site.each_context(request)
        contexto['form'] = form
        
        
        return render(request, "constancias/carga_csv_form.html", contexto)


   



admin.site.register(Participante, ParticipanteAdmin)


admin.site.register(Evento)
admin.site.register(Plantilla)
admin.site.register(Constancia)
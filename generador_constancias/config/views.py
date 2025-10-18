from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'mensaje': 'Sistema de Generación de Constancias Universitarias - En Desarrollo'
    })
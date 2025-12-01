from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from constancias.models import Evento, Participante

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

@login_required
def dashboard_view(request):
    # Obtener eventos activos (próximos o en curso)
    hoy = timezone.now().date()
    eventos_activos = Evento.objects.filter(
        fecha_inicio__gte=hoy - timedelta(days=7),
        activo=True
    ).order_by('fecha_inicio')[:6]
    
    # Estadísticas básicas
    total_eventos = Evento.objects.count()
    total_participantes = Participante.objects.count()
    eventos_este_mes = Evento.objects.filter(
        fecha_inicio__month=hoy.month,
        fecha_inicio__year=hoy.year
    ).count()
    
    contexto = {
        'user': request.user,
        'eventos_activos': eventos_activos,
        'total_eventos': total_eventos,
        'total_participantes': total_participantes,
        'eventos_este_mes': eventos_este_mes,
    }
    
    return render(request, 'usuarios/dashboard.html', contexto)

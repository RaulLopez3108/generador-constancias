"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from constancias import views as constancias_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('participantes/',constancias_views.lista_participantes, name='lista_participantes'),
    path('participantes/<int:pk>/',constancias_views.detalle_participante,name='detalle_participante'),
    path('eventos/',constancias_views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:pk>/',constancias_views.detalle_evento,name='detalle_evento')
]

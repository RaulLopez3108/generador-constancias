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
from django.conf import settings
from django.conf.urls.static import static
from constancias import views as constancias_views
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', usuarios_views.login_view, name='login'),
    path('login/', usuarios_views.login_view, name='login'),
    path('logout/', usuarios_views.logout_view, name='logout'),
    path('dashboard/', usuarios_views.dashboard_view, name='dashboard'),
    
    # Test URL
    path('test-post/', constancias_views.test_post_view, name='test_post'),
    
    # URLs de constancias (protegidas)
    path('participantes/',constancias_views.lista_participantes, name='lista_participantes'),
    path('participantes/gestionar/', constancias_views.gestionar_participantes, name='gestionar_participantes'),
    path('participantes/crear/', constancias_views.crear_participante_individual, name='crear_participante_individual'),
    path('participantes/cargar-csv/', constancias_views.cargar_participantes_csv, name='cargar_participantes_csv'),
    path('participantes/descargar-plantilla-csv/', constancias_views.descargar_plantilla_csv, name='descargar_plantilla_csv'),
    path('participantes/<int:pk>/',constancias_views.detalle_participante,name='detalle_participante'),
    path('participantes/<int:pk>/eliminar/', constancias_views.eliminar_participante, name='eliminar_participante'),
    path('participantes/exportar-csv/', constancias_views.exportar_participantes_csv, name='exportar_participantes_csv'),
    path('eventos/<int:evento_pk>/participantes/<int:participante_pk>/eliminar/', 
         constancias_views.eliminar_participante_de_evento, name='eliminar_participante_de_evento'),
    path('eventos/<int:evento_pk>/participantes/exportar-csv/', 
         constancias_views.exportar_participantes_evento_csv, name='exportar_participantes_evento_csv'),
    path('eventos/',constancias_views.lista_eventos, name='lista_eventos'),
    path('eventos/crear/', constancias_views.crear_evento, name='crear_evento'),
    path('eventos/<int:pk>/',constancias_views.detalle_evento,name='detalle_evento'),
    path('eventos/<int:pk>/editar/', constancias_views.editar_evento, name='editar_evento'),
    path('eventos/<int:pk>/eliminar/', constancias_views.eliminar_evento, name='eliminar_evento'),
    path('api/eventos/<int:evento_pk>/participantes/', constancias_views.api_participantes_evento, name='api_participantes_evento'),
    path('generar/', constancias_views.pagina_generar_constancia, name='pagina_generar'),
    path('generar/<int:participante_pk>/<int:evento_pk>/<int:plantilla_pk>/', 
     constancias_views.generar_constancia, name='generar_constancia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

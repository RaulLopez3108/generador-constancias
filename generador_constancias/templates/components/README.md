# Componente Navbar - Certif Kit

## 📋 Uso del Componente

### Implementación Básica
Para usar la navbar en cualquier página, simplemente incluye el componente:

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
{% include 'components/navbar.html' %}

<!-- Tu contenido aquí -->
<div class="container-fluid px-4">
    <!-- Content with top margin for fixed navbar -->
</div>
{% endblock %}
```

### 🎨 Características del Componente

#### ✨ Funcionalidades Automáticas:
- **Auto-hide**: Se esconde al hacer scroll down, aparece al hacer scroll up
- **Mouse Detection**: Aparece al acercar el mouse a la parte superior
- **Active States**: Resalta automáticamente la página actual
- **Responsive Design**: Se adapta a dispositivos móviles

#### 🎯 Enlaces Incluidos:
- **Home**: Dashboard principal
- **Eventos**: Lista de eventos
- **Participantes**: Lista de participantes
- **Admin**: Panel Django (nueva pestaña)
- **Salir**: Logout del sistema

### 🛠️ Personalización

#### Modificar Enlaces:
Edita `/templates/components/navbar.html`:

```html
<a class="nav-link {% if request.resolver_match.url_name == 'tu_vista' %}active{% endif %}" href="{% url 'tu_vista' %}">
    <i class="fas fa-tu-icono"></i>
    <span>Tu Texto</span>
</a>
```

#### Agregar Nuevos Enlaces:
```html
<a class="nav-link" href="{% url 'nueva_vista' %}">
    <i class="fas fa-nuevo-icono"></i>
    <span>Nueva Sección</span>
</a>
```

### 📱 Comportamiento Responsive

#### Desktop:
- Logo + texto completo
- Todos los enlaces visibles con iconos y texto

#### Mobile/Tablet:
- Logo más pequeño
- Solo iconos visibles, texto oculto
- Espaciado optimizado

### 🎨 Estilos Disponibles

#### Variables CSS Utilizadas:
```css
--trustec-green: #22c55e
--dark-gray: #1f2937
--medium-gray: #334155
--text-secondary: #cbd5e1
```

#### Clases CSS del Componente:
- `.modern-navbar`: Container principal
- `.navbar-logo`: Logo de Trustec
- `.brand-text`: Texto "Certif Kit"
- `.nav-link`: Enlaces de navegación
- `.nav-link.active`: Estado activo
- `.logout-link`: Enlace de salir (estilo especial)

### 🔧 JavaScript Incluido

#### Funciones Automáticas:
1. **Scroll Detection**: Detecta dirección del scroll
2. **Mouse Proximity**: Muestra navbar al acercar mouse
3. **Auto-Hide Timer**: Se esconde después de inactividad
4. **Smooth Animations**: Transiciones fluidas

### 📖 Ejemplo Completo

```html
<!-- En tu template de página -->
{% extends 'base.html' %}
{% load static %}

{% block title %}Tu Página - Certif Kit{% endblock %}

{% block extra_css %}
<style>
    /* Asegurar espacio para navbar fija */
    body {
        padding-top: 70px;
    }
    
    /* Tus estilos específicos */
    .tu-contenido {
        margin-top: 2rem;
    }
</style>
{% endblock %}

{% block content %}
{% include 'components/navbar.html' %}

<div class="container-fluid px-4">
    <h1>Tu contenido aquí</h1>
    <!-- Resto de tu página -->
</div>
{% endblock %}
```

### 🚀 Ventajas del Componente

1. **Reutilizable**: Un solo archivo para todas las páginas
2. **Mantenible**: Cambios centralizados
3. **Consistente**: Mismo diseño en toda la aplicación
4. **Funcional**: Auto-hide y detección inteligente
5. **Responsive**: Se adapta a todos los dispositivos
6. **Accessible**: Estados activos automáticos

### 🔄 Actualización del Componente

Para modificar la navbar en todas las páginas:
1. Edita `/templates/components/navbar.html`
2. Los cambios se aplican automáticamente a todas las páginas que lo incluyan

### 💡 Tips de Uso

- Siempre agregar `padding-top: 70px` al body en páginas que usen navbar fija
- Usar `container-fluid px-4` para aprovechar toda la pantalla
- El estado activo se detecta automáticamente por `request.resolver_match.url_name`
- El componente incluye todos los estilos CSS y JavaScript necesarios
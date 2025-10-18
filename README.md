# Generador de Constancias

Sistema administrativo para la generación automática de constancias.

## Arquitectura del Proyecto

### Tecnologías Utilizadas
- **Framework**: Django 5.2.7
- **Lenguaje**: Python 3.10+
- **Gestión de Dependencias**: UV
- **Base de Datos**: SQLite (desarrollo)
- **Generación PDF**: Por definir

### Aplicaciones Django
1. **`usuarios`** - Gestión de autenticación y roles administrativos
2. **`eventos`** - CRUD y gestión de eventos universitarios  
3. **`constancias`** - Generación y registro de constancias PDF

## Configuración del Entorno de Desarrollo

### Requisitos Previos
- Python 3.10 o superior
- UV instalado ([Guía de instalación](https://docs.astral.sh/uv/getting-started/installation/))
- Git

### 1. Clonar el Repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd generador-constancias
```

### 2. Configurar el Entorno
```bash
# Sincronizar dependencias del workspace
uv sync

# Navegar al directorio del proyecto Django
cd generador_constancias
```

### 3. Configurar la Base de Datos
```bash
# Aplicar migraciones
uv run python manage.py migrate

# Crear superusuario para el panel administrativo
uv run python manage.py createsuperuser
```
En este paso ingresa el nombre de usuario, correo electrónico y contraseña del admin que quieras

### 4. Ejecutar el Servidor de Desarrollo
```bash
uv run python manage.py runserver
```

### 5. Acceder al Sistema
- **Página Principal**: http://127.0.0.1:8000/
- **Panel de Administración**: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
generador-constancias/
├── pyproject.toml                 # Configuración del workspace
├── generador_constancias/         # Proyecto Django principal
│   ├── config/                    # Configuración del proyecto
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── usuarios/                  # App: Gestión de usuarios
│   ├── eventos/                   # App: Gestión de eventos
│   ├── constancias/              # App: Generación de constancias
│   ├── templates/                # Plantillas HTML
│   ├── static/                   # Archivos estáticos
│   ├── media/                    # Archivos generados (PDFs)
│   └── manage.py
└── README.md
```

## Control de Acceso

- **Sistema Administrativo**: Solo administradores y organizadores tienen acceso
- **Participantes**: NO tienen acceso directo al sistema
- **Panel de Administración**: Interfaz principal para gestión


## Documentación Adicional

- [Documentación Django](https://docs.djangoproject.com/)
- [Documentación UV](https://docs.astral.sh/uv/)

## Progreso

- Estructura básica implementada (desarrollada)
- Interfaz de datos (pendiente)
- Funcion de agregar (pendiente)
- Funciones de busqueda (pendiente)
- Funciones de actualizaciones (pendiente)
- Generacion de certificados (pendeiente)
- Entrega de certificados (pendiente)


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣴⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠉⠉⠙⠻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠀⠀⠀⠙⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠃⠀⣠⡤⢄⡀⠀⠙⢷⣄⢀⣀⣀⣀⣾⢦⡿⣡⡶⣂⣀⣀⣴⠟⠁⠀⣠⠖⢋⠶⡀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⢰⠇⣽⣀⡻⣦⠀⠈⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⢼⣭⣞⣇⣴⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢸⡃⢠⢷⡱⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢽⣴⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠘⢶⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣌⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡆⠀⠈⠓⣄⠀⠀⠀⠀⡴⠁⠀⠀⠖⠒⠒⠢⢤⡀⠀⠙⣿⡛⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⠇⠀⠀⠀⢀⡠⠎⠀⠀⠀⢀⣀⣀⣀⡀⠀⠘⣶⠾⠿⣶⡇⠀⣀⣤⣤⣄⣀⡀⠀⠙⠲⡄⢹⣟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⡤⠋⠀⠀⣠⡴⠚⠏⠉⠉⠙⠉⠢⣤⡇⠀⠀⠈⢧⡾⠋⠁⠀⡀⠀⠋⢷⣄⠀⠘⢦⢻⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⢀⡤⠊⠀⢀⣴⠾⠋⠀⠀⢀⣤⣤⣄⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⡄⠀⠀⠛⢿⣄⠀⠑⢽⣧⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠟⠔⠒⠉⠀⠀⣰⠟⠁⠀⠀⠀⠀⣾⣿⣿⣿⡆⣀⣤⣤⡄⠀⡀⣤⣤⣶⣿⣿⣿⣿⠀⠀⠀⠀⠻⣧⠀⠀⢨⣍⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠙⠿⠟⣁⠞⠉⠀⠀⣿⣿⣿⣿⡆⠀⠙⣿⠋⠁⠀⠀⠀⠀⠀⢻⡇⠀⠀⣽⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡄⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⠀⠉⠛⣿⠋⠀⠀⣀⠈⠻⢄⡀⠀⠀⢀⡰⠏⠀⠀⢠⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠉⠳⠤⢤⣤⡤⠤⠚⠁⠀⠀⣸⣷⣦⣤⣴⠾⠻⠶⠶⠾⠛⠷⣦⡀⠀⠉⠉⠁⠀⠀⠀⣠⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⠁⣀⣀⠀⠀⠀⢶⠄⠀⢀⣤⡌⠻⣧⡀⠀⠀⢀⣠⡾⠟⠁⠀⠀⠀⠀⠀
⠀⠀⣤⣴⣾⠿⠒⠳⢶⣤⡀⠀⠀⢨⣿⠛⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠿⠿⠀⠀⠀⠀⠀⠀⠈⠛⠃⢀⣸⣧⣀⠰⠛⣿⠗⠀⠀⠀⠀⠀⠀⠀
⠀⣴⡟⠉⠀⠀⠀⢀⠀⠉⢿⣄⠀⠐⣿⠂⠀⠀⠀⠀⠀⣀⣀⣀⣤⡾⠟⣛⣻⣿⣄⠀⠀⠀⠇⠀⠀⣠⣄⠀⢠⡿⠿⡯⠻⢷⣄⣙⢷⡄⠀⠀⠀⠀⠀⠀
⢸⣏⠃⠀⠀⠀⣠⠖⠶⠞⠋⣿⣀⣾⠏⠀⠀⠀⠀⠀⠈⠉⠉⢻⡋⠀⠀⠈⢩⣴⣿⣄⣴⣤⠀⠀⠀⠟⠛⠀⣿⡿⣶⠀⠀⠀⡿⠉⠈⢻⡆⠀⠀⠀⠀⠀
⣿⡯⠴⠋⠉⠉⠁⠀⠀⢀⣀⢸⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⣠⡿⠋⠛⠋⠀⠀⠀⢀⣀⠀⠛⣷⡔⠀⠀⣠⠟⠀⠀⢸⣿⠀⠀⠀⠀⠀
⣿⡇⠀⠀⡀⣠⠖⠒⠖⠋⢩⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⡀⠀⣼⡟⠀⠀⠀⠀⣦⠀⠀⠿⠿⠀⢠⣾⣷⡶⠿⠋⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀
⣿⣇⣴⠋⠉⠉⠀⠀⠄⠀⣼⠇⠀⠀⠀⠀⢠⣄⠀⠀⠀⠀⠀⠀⠀⢀⣨⣿⠋⠛⢷⣤⣤⣀⣀⣀⣀⣠⣤⡿⠛⠀⠘⠻⣦⣤⣀⣤⣴⠿⣷⣄⠀⠀⠀⠀
⣿⣷⠀⠀⠀⢀⣀⡰⠛⠙⣿⠀⠀⠀⠀⠀⠈⠙⠷⠶⢶⣤⣶⣶⠾⠟⠉⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠹⠉⠉⠀⠀⠀⠻⣧⠀⠀⠀
⢸⣇⠀⣀⣴⠉⠁⠀⠀⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠀⠠⡇⠀⠀⠀⠀⠀⢹⡇⠀⠀
⠈⢿⡏⠀⠀⠀⠀⣀⣾⡙⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠈⢻⣆⠀⠀⡞⠃⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⢀⣠⣤⣤⣿⣁⠀⠀
⠀⠀⠀⠙⢷⣴⣇⠀⠀⢀⡟⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠶⠛⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⢀⣴⠿⠋⠁⢴⣗⢻⣿⣷⡀
⠀⠀⠀⠀⠀⠉⠻⠶⣶⣿⣀⣈⣿⣦⡀⠀⠀⠀⠀⢀⡴⠋⠁⠀⢰⣤⡘⣦⣹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣶⣯⣄⣠⣿⡀⠀⠀⠀⠀⢙⣷⣿⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠷⣦⣤⣄⣸⣃⠀⠀⠀⠀⣸⣧⣼⣿⠟⠓⠶⠶⠶⠾⠛⠛⠛⠛⠉⠉⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠙⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# Importo el panel de administración de Django
from django.contrib import admin

# Importo path e include para poder conectar rutas entre apps
from django.urls import path, include


# Aquí defino las rutas principales del proyecto
urlpatterns = [

    # Ruta del panel de administración
    path('admin/', admin.site.urls),

    # Aquí conecto las URLs de mi aplicación "tareas"
    # Esto permite que Django use el archivo tareas/urls.py
    path('', include('tareas.urls')),
]# Importo el panel de administración de Django
from django.contrib import admin

# Importo path e include para poder conectar rutas entre apps
from django.urls import path, include


# Aquí defino las rutas principales del proyecto
urlpatterns = [

    # Ruta del panel de administración
    path('admin/', admin.site.urls),

    # Aquí conecto las URLs de mi aplicación "tareas"
    # Esto permite que Django use el archivo tareas/urls.py
    path('', include('tareas.urls')),
]
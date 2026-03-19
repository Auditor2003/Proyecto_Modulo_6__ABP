# Importo el panel de administración que trae Django
from django.contrib import admin

# Importo las funciones necesarias para manejar rutas
from django.urls import path, include

# Aquí defino las rutas principales de todo mi proyecto
urlpatterns = [

    # Esta ruta permite acceder al panel de administración de Django
    path('admin/', admin.site.urls),

    # Aquí conecto las URLs de mi aplicación "tareas"
    # Esto le dice a Django que use el archivo tareas/urls.py
    path('', include('tareas.urls')),
]
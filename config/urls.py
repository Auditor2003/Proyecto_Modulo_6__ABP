# Aquí importo el panel de administración de Django
from django.contrib import admin

# Aquí importo la función path para definir rutas
from django.urls import path

# Aquí importo las vistas que voy a usar
from tareas.views import home, dashboard, registro, CustomLoginView, CustomLogoutView


# Aquí defino todas las rutas del proyecto
urlpatterns = [

    # Aquí dejo acceso al panel de administración
    path('admin/', admin.site.urls),

    # Aquí defino la ruta del home (pantalla principal)
    path('', home, name='home'),

    # Aquí defino la ruta del dashboard (detalle de proyectos)
    path('dashboard/', dashboard, name='dashboard'),

    # Aquí defino la ruta del login
    path('login/', CustomLoginView.as_view(), name='login'),

    # Aquí defino la ruta del logout
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Aquí defino la ruta del registro de usuarios
    path('registro/', registro, name='registro'),
]
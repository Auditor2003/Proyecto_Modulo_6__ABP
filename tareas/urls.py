# Importo path para crear rutas
from django.urls import path

# Importo las vistas de mi aplicación
from . import views


# Aquí defino las rutas propias de la aplicación tareas
urlpatterns = [

    # Página de inicio
    path('', views.home, name='home'),

]
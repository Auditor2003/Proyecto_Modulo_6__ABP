# Importo la función path para poder definir rutas dentro de mi aplicación
from django.urls import path

# Importo las vistas que definí en el archivo views.py
from . import views


# Aquí defino las URLs de mi aplicación "tareas"
urlpatterns = [

    # Aquí defino la ruta de la página principal (home)
    # Esta ruta llama a la vista home que se encuentra en views.py
    path('', views.home, name='home'),

    # Aquí defino la ruta del dashboard
    # Esta vista está protegida con el decorador login_required
    # por lo tanto solo usuarios autenticados podrán acceder
    path('dashboard/', views.dashboard, name='dashboard'),

]
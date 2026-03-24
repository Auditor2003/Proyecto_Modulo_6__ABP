# Importo la función path para poder definir rutas dentro de mi aplicación
from django.urls import path

# Importo las vistas que definí en el archivo views.py
from . import views


# Aquí defino las URLs de mi aplicación "tareas"
urlpatterns = [

    # Aquí defino la ruta de la página principal
    path('', views.home, name='home'),

    # Aquí defino la ruta del dashboard
    # Esta vista está protegida y solo permite acceso a usuarios autenticados
    path('dashboard/', views.dashboard, name='dashboard'),

    # Aquí defino la ruta del login
    # Uso la vista basada en clases que creé para iniciar sesión
    path('login/', views.CustomLoginView.as_view(), name='login'),

]
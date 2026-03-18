# Importo la función path que me permite definir rutas dentro de mi aplicación
from django.urls import path

# Importo las vistas que definí en views.py
# Desde aquí podré conectar las rutas con las funciones que muestran las páginas
from . import views


# Aquí defino la lista de rutas (URL patterns) que tendrá mi aplicación
urlpatterns = [

    # Esta será la página principal de mi aplicación
    # Cuando el usuario entre a la raíz del sitio ( / )
    # Django ejecutará la función "home" que definí en views.py
    path('', views.home, name='home'),

]
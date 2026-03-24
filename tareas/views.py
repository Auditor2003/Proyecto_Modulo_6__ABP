# Importo la función render para poder mostrar páginas HTML
from django.shortcuts import render

# Importo el decorador login_required
# Este decorador me permite proteger vistas para que solo entren usuarios autenticados
from django.contrib.auth.decorators import login_required

# Importo la vista LoginView y la vista LogoutView que Django trae listas
# para manejar el inicio y cierre de sesión
from django.contrib.auth.views import LoginView, LogoutView

# Importo reverse_lazy para poder redirigir a una ruta después del login
from django.urls import reverse_lazy


# VISTA HOME

# Aquí defino la página principal de mi aplicación
def home(request):

    # Aquí renderizo la plantilla principal home.html
    return render(request, 'tareas/home.html')


# VISTA DASHBOARD

# Aquí protejo esta vista para que solo usuarios logueados puedan acceder
@login_required
def dashboard(request):

    # Aquí renderizo la plantilla del dashboard
    return render(request, 'tareas/dashboard.html')


# VISTA LOGIN
#
# Aquí creo una vista basada en clases para manejar el inicio de sesión
class CustomLoginView(LoginView):

    # Aquí indico qué plantilla HTML voy a usar para mostrar el login
    template_name = 'tareas/login.html'

    # Aquí indico que después de iniciar sesión quiero ir al dashboard
    success_url = reverse_lazy('dashboard')


# VISTA LOGOUT
# 
# Aquí creo una vista basada en clases para cerrar la sesión del usuario
class CustomLogoutView(LogoutView):

    # Aquí indico a qué página quiero enviar al usuario después de cerrar sesión
    next_page = 'home'
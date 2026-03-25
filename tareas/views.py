# Importo la función render para poder mostrar páginas HTML
from django.shortcuts import render

# Importo el decorador login_required
from django.contrib.auth.decorators import login_required

# Importo vistas de autenticación
from django.contrib.auth.views import LoginView, LogoutView

# Importo reverse_lazy para redirecciones
from django.urls import reverse_lazy

# Importo mis modelos
from .models import Proyecto, Tarea


# Aquí defino la página principal de mi aplicación
def home(request):

    # Aquí cuento la cantidad total de proyectos
    total_proyectos = Proyecto.objects.count()

    # Aquí cuento la cantidad total de tareas
    total_tareas = Tarea.objects.count()

    # Aquí cuento solo las tareas pendientes (no completadas)
    pendientes = Tarea.objects.filter(completado=False).count()

    # Aquí envío estos datos al template
    return render(request, 'tareas/home.html', {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'pendientes': pendientes
    })


# Aquí protejo esta vista
@login_required
def dashboard(request):
    return render(request, 'tareas/dashboard.html')


# Vista login personalizada
class CustomLoginView(LoginView):
    template_name = 'tareas/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')


# Vista logout personalizada
class CustomLogoutView(LogoutView):
    next_page = 'home'
# Importo la función render para poder devolver templates
from django.shortcuts import render

# Importo el decorador para proteger vistas
from django.contrib.auth.decorators import login_required

# Importo vistas de autenticación de Django
from django.contrib.auth.views import LoginView, LogoutView

# Importo reverse_lazy para redirecciones
from django.urls import reverse_lazy

# Importo mis modelos
from .models import Proyecto, Tarea


# Aquí defino la vista del home
def home(request):

    # Aquí cuento la cantidad total de proyectos
    total_proyectos = Proyecto.objects.count()

    # Aquí cuento la cantidad total de tareas
    total_tareas = Tarea.objects.count()

    # Aquí cuento solo las tareas pendientes
    pendientes = Tarea.objects.filter(completado=False).count()

    # Aquí envío los datos al template
    return render(request, 'tareas/home.html', {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'pendientes': pendientes
    })


# Aquí protejo la vista del dashboard
@login_required
def dashboard(request):

    # Aquí verifico si el usuario es superusuario
    if request.user.is_superuser:

        # Aquí obtengo todos los proyectos
        proyectos = Proyecto.objects.all()

        # Aquí envío los proyectos al template
        return render(request, 'tareas/dashboard.html', {
            'proyectos': proyectos
        })

    else:
        # Aquí si es usuario normal no envío detalle
        return render(request, 'tareas/dashboard.html')


# Aquí defino la vista de login personalizada
class CustomLoginView(LoginView):

    # Aquí indico qué template usar
    template_name = 'tareas/login.html'

    # Aquí defino a dónde redirigir después del login
    def get_success_url(self):
        return reverse_lazy('dashboard')


# Aquí defino la vista de logout personalizada
class CustomLogoutView(LogoutView):

    # Aquí defino a dónde redirigir después del logout
    next_page = 'home'
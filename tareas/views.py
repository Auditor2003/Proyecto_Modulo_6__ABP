# Importo la función render para devolver templates
from django.shortcuts import render

# Importo decorador para proteger vistas
from django.contrib.auth.decorators import login_required

# Importo vistas de autenticación
from django.contrib.auth.views import LoginView, LogoutView

# Importo reverse_lazy para redirecciones
from django.urls import reverse_lazy

# Importo modelos
from .models import Proyecto, Tarea


# Aquí defino el HOME (dashboard visual con conteos)
def home(request):

    # Aquí cuento proyectos
    total_proyectos = Proyecto.objects.count()

    # Aquí cuento tareas
    total_tareas = Tarea.objects.count()

    # Aquí cuento pendientes
    pendientes = Tarea.objects.filter(completado=False).count()

    # Aquí renderizo el home
    return render(request, 'tareas/home.html', {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'pendientes': pendientes
    })


# Aquí defino el DASHBOARD real (detalle)
@login_required
def dashboard(request):

    # Aquí verifico si es superusuario
    if request.user.is_superuser:

        # Aquí obtengo proyectos con sus tareas
        proyectos = Proyecto.objects.all()

        return render(request, 'tareas/dashboard.html', {
            'proyectos': proyectos
        })

    else:
        # Aquí usuario normal entra pero sin detalle
        return render(request, 'tareas/dashboard.html')


# Aquí defino login personalizado
class CustomLoginView(LoginView):

    # Aquí uso mi template
    template_name = 'tareas/login.html'

    # Aquí defino que SIEMPRE vuelva al home (conteos)
    def get_success_url(self):
        return reverse_lazy('home')


# Aquí defino logout
class CustomLogoutView(LogoutView):

    # Aquí redirijo al home
    next_page = 'home'
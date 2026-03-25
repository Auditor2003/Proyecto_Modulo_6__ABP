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


# Aquí defino la vista del home
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


# Aquí protejo el dashboard (si no está logueado lo manda a login)
@login_required
def dashboard(request):

    # Aquí verifico si es superusuario
    if request.user.is_superuser:

        # Aquí obtengo proyectos
        proyectos = Proyecto.objects.all()

        # Aquí renderizo con detalle
        return render(request, 'tareas/dashboard.html', {
            'proyectos': proyectos
        })

    else:
        # Aquí renderizo sin detalle
        return render(request, 'tareas/dashboard.html')


# Aquí defino login personalizado
class CustomLoginView(LoginView):

    # Aquí indico template
    template_name = 'tareas/login.html'

    # Aquí dejo que Django maneje el next automáticamente
    def get_success_url(self):

        # Aquí reviso si existe "next"
        next_url = self.request.GET.get('next')

        # Si existe, lo uso
        if next_url:
            return next_url

        # Si no, lo mando al dashboard
        return reverse_lazy('dashboard')


# Aquí defino logout
class CustomLogoutView(LogoutView):

    # Aquí lo mando al home al cerrar sesión
    next_page = 'home'
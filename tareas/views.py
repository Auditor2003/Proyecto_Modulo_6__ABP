# Importo render y redirect
from django.shortcuts import render, redirect

# Importo decorador para proteger vistas
from django.contrib.auth.decorators import login_required

# Importo vistas de autenticación
from django.contrib.auth.views import LoginView, LogoutView

# Importo reverse_lazy
from django.urls import reverse_lazy

# Importo modelos
from .models import Proyecto, Tarea

# Importo formulario de registro
from .forms import RegistroUsuarioForm


# Aquí defino el home (pantalla principal con conteo)
def home(request):

    # Aquí cuento proyectos
    total_proyectos = Proyecto.objects.count()

    # Aquí cuento tareas
    total_tareas = Tarea.objects.count()

    # Aquí cuento pendientes
    pendientes = Tarea.objects.filter(completado=False).count()

    # Aquí envío datos al template
    return render(request, 'tareas/home.html', {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'pendientes': pendientes
    })


# Aquí defino el dashboard (detalle)
@login_required
def dashboard(request):

    # Aquí verifico si es superusuario
    if request.user.is_superuser:

        # Aquí obtengo todos los proyectos
        proyectos = Proyecto.objects.all()

    else:
        # Aquí solo obtengo los proyectos del usuario
        proyectos = Proyecto.objects.filter(usuario=request.user)

    # Aquí renderizo
    return render(request, 'tareas/dashboard.html', {
        'proyectos': proyectos
    })


# Aquí creo la vista de registro
def registro(request):

    # Aquí verifico si es POST
    if request.method == 'POST':

        form = RegistroUsuarioForm(request.POST)

        # Aquí valido el formulario
        if form.is_valid():

            # Aquí creo usuario sin guardar aún
            user = form.save(commit=False)

            # Aquí obtengo datos
            tipo = form.cleaned_data['tipo_usuario']
            proyecto = form.cleaned_data['proyecto']

            # Aquí asigno tipo de usuario
            if tipo == 'admin':
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False

            # Aquí guardo el usuario
            user.save()

            # Aquí asigno el proyecto al usuario
            proyecto.usuario = user
            proyecto.save()

            # Aquí redirijo al login
            return redirect('login')

    else:
        form = RegistroUsuarioForm()

    # Aquí renderizo el formulario
    return render(request, 'tareas/registro.html', {
        'form': form
    })


# Aquí defino login personalizado
class CustomLoginView(LoginView):

    template_name = 'tareas/login.html'

    # Aquí redirijo al home
    def get_success_url(self):
        return reverse_lazy('home')


# Aquí defino logout
class CustomLogoutView(LogoutView):

    # Aquí redirijo al home
    next_page = 'home'
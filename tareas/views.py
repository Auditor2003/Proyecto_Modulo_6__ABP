from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .models import Proyecto, Tarea
from .forms import RegistroUsuarioForm, CustomAuthenticationForm


def home(request):
    total_proyectos = Proyecto.objects.count()
    total_tareas = Tarea.objects.count()
    pendientes = Tarea.objects.filter(completado=False).count()

    return render(request, 'tareas/home.html', {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'pendientes': pendientes
    })


@login_required
def dashboard(request):

    if request.user.is_superuser:
        proyectos = Proyecto.objects.all()
    else:
        proyectos = Proyecto.objects.filter(usuario=request.user)

    return render(request, 'tareas/dashboard.html', {
        'proyectos': proyectos
    })


def registro(request):

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            tipo = form.cleaned_data['tipo_usuario']
            proyecto = form.cleaned_data['proyecto']

            if tipo == 'admin':
                user.is_superuser = True
                user.is_staff = True
            else:
                user.is_superuser = False
                user.is_staff = False

            user.save()

            proyecto.usuario = user
            proyecto.save()

            return redirect('login')

    else:
        form = RegistroUsuarioForm()

    return render(request, 'tareas/registro.html', {
        'form': form
    })


class CustomLoginView(LoginView):

    template_name = 'tareas/login.html'

    # AQUÍ CONECTO EL FORM BONITO
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('home')


class CustomLogoutView(LogoutView):
    next_page = 'home'
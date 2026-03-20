# Importo la función render para poder mostrar páginas HTML
from django.shortcuts import render

# Importo el decorador login_required
# Este decorador permite que solo usuarios logueados puedan acceder a ciertas vistas
from django.contrib.auth.decorators import login_required


# 
# 
# Esta es la página principal del sitio
# Cualquier usuario puede verla, incluso si no está logueado
def home(request):

    # Renderizo la plantilla home.html
    return render(request, 'tareas/home.html')


# 
# VISTA DASHBOARD
# 
# Uso el decorador login_required para proteger esta vista
# Esto significa que solo usuarios autenticados pueden acceder
@login_required
def dashboard(request):

    # Aquí renderizo la página dashboard.html
    return render(request, 'tareas/dashboard.html')
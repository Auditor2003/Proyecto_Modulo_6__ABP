# Importo la función render para mostrar plantillas HTML
from django.shortcuts import render

# Importo mis modelos para poder consultar datos de la base de datos
from .models import Proyecto, Tarea


# Aquí defino la vista de la página principal
def home(request):

    # Aquí cuento cuántos proyectos existen en la base de datos
    total_proyectos = Proyecto.objects.count()

    # Aquí cuento cuántas tareas existen
    total_tareas = Tarea.objects.count()

    # Aquí cuento las tareas pendientes
    tareas_pendientes = Tarea.objects.filter(completada=False).count()

    # Aquí envío los datos al template para mostrarlos en la página
    contexto = {
        'total_proyectos': total_proyectos,
        'total_tareas': total_tareas,
        'tareas_pendientes': tareas_pendientes
    }

    return render(request, 'tareas/home.html', contexto)
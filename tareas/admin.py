# Importo el módulo admin de Django
# Esto me permite registrar modelos para administrarlos desde el panel admin
from django.contrib import admin

# Importo los modelos que creé en models.py
from .models import Proyecto, Tarea


# Aquí registro el modelo Proyecto en el panel de administración
# Esto me permitirá crear, editar y eliminar proyectos desde el admin
admin.site.register(Proyecto)


# Aquí registro el modelo Tarea en el panel de administración
# Esto me permitirá gestionar las tareas desde el admin
admin.site.register(Tarea)
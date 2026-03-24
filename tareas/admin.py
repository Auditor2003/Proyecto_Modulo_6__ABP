# Importo el módulo admin de Django
from django.contrib import admin

# Importo mis modelos Proyecto y Tarea
from .models import Proyecto, Tarea


# Aquí registro el modelo Proyecto para poder verlo en el panel de administración
admin.site.register(Proyecto)

# Aquí registro el modelo Tarea para poder verlo en el panel de administración
admin.site.register(Tarea)
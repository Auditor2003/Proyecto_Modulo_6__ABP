# Importo models para poder crear mis tablas en la base de datos
from django.db import models


# MODELO PROYECTO

# Aquí defino el modelo Proyecto
class Proyecto(models.Model):

    # Aquí guardo el nombre del proyecto
    nombre = models.CharField(max_length=100)

    # Aquí guardo una descripción del proyecto
    descripcion = models.TextField()

    # Aquí guardo la fecha de creación automáticamente
    creado = models.DateTimeField(auto_now_add=True)

    # Aquí defino cómo se verá el proyecto en el admin
    def __str__(self):
        return self.nombre


# MODELO TAREA

# Aquí defino el modelo Tarea
class Tarea(models.Model):

    # Aquí guardo el nombre de la tarea
    nombre = models.CharField(max_length=100)

    # Aquí guardo una descripción de la tarea
    descripcion = models.TextField()

    # Aquí relaciono la tarea con un proyecto (clave foránea)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    # Aquí indico si la tarea está completada o no
    completado = models.BooleanField(default=False)

    # Aquí guardo la fecha de creación automáticamente
    creado = models.DateTimeField(auto_now_add=True)

    # Aquí defino cómo se verá la tarea en el admin
    def __str__(self):
        return self.nombre
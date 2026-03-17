# Importo el módulo de modelos de Django.
# Esto me permite definir la estructura de las tablas que se guardarán en la base de datos.
from django.db import models

# Importo el modelo de usuario que trae Django por defecto.
# Lo usaré para relacionar los proyectos con el usuario que los crea.
from django.contrib.auth.models import User


# MODELO PROYECTO
#
# En este modelo defino la estructura de un proyecto dentro del sistema.
# La idea es que cada usuario pueda crear y gestionar sus propios proyectos.
class Proyecto(models.Model):

    # Aquí guardo el nombre del proyecto.
    # Uso CharField porque es un texto corto.
    nombre = models.CharField(max_length=200)

    # Aquí guardo una descripción más detallada del proyecto.
    # Uso TextField porque permite textos más largos.
    descripcion = models.TextField()

    # Aquí creo la relación entre el proyecto y el usuario que lo creó.
    # Uso ForeignKey porque un usuario puede tener varios proyectos.
    # Si el usuario se elimina, también se eliminarán sus proyectos.
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Este método define cómo se mostrará el proyecto cuando lo vea en el panel de administración.
    def __str__(self):
        return self.nombre

# MODELO TAREA
# 
# En este modelo defino las tareas que pertenecen a un proyecto.
# Un proyecto puede tener muchas tareas asociadas.
class Tarea(models.Model):

    # Aquí guardo el título de la tarea.
    titulo = models.CharField(max_length=200)

    # Aquí guardo la descripción de la tarea.
    descripcion = models.TextField()

    # Esta variable indica si la tarea está completada o no.
    # Uso BooleanField porque solo puede ser True o False.
    # Por defecto la tarea se crea como no completada.
    completada = models.BooleanField(default=False)

    # Aquí relaciono cada tarea con el proyecto al que pertenece.
    # Esto permite que un proyecto tenga muchas tareas.
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    # Este método define cómo se mostrará la tarea en el panel de administración.
    def __str__(self):
        return self.titulo
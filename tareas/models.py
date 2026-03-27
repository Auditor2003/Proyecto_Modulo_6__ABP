# Importo models
from django.db import models

# Importo modelo User
from django.contrib.auth.models import User


# Aquí defino modelo Proyecto
class Proyecto(models.Model):

    # Nombre del proyecto
    nombre = models.CharField(max_length=100)

    # Aquí relaciono proyecto con usuario
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    # Representación
    def __str__(self):
        return self.nombre


# Aquí defino modelo Tarea
class Tarea(models.Model):

    nombre = models.CharField(max_length=100)

    completado = models.BooleanField(default=False)

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
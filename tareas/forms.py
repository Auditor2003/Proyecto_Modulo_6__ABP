# Importo formularios
from django import forms

# Importo modelo User
from django.contrib.auth.models import User

# Importo formulario base
from django.contrib.auth.forms import UserCreationForm

# Importo modelo Proyecto
from .models import Proyecto


# Aquí creo formulario de registro
class RegistroUsuarioForm(UserCreationForm):

    # Aquí defino tipo de usuario
    TIPO_USUARIO = (
        ('normal', 'Usuario normal'),
        ('admin', 'Administrador'),
    )

    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO)

    # Aquí permito elegir proyecto
    proyecto = forms.ModelChoiceField(queryset=Proyecto.objects.all())

    class Meta:
        model = User

        # Campos del formulario
        fields = ['username', 'password1', 'password2']
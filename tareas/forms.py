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

    tipo_usuario = forms.ChoiceField(
        choices=TIPO_USUARIO,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    # Aquí permito elegir proyecto
    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User

        # Campos
        fields = ['username', 'password1', 'password2']

        # AQUÍ ESTÁ LA CLAVE DEL ARREGLO VISUAL
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # AQUÍ ARREGLO LOS PASSWORD (clave)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aquí agrego clases Bootstrap a todos los campos
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
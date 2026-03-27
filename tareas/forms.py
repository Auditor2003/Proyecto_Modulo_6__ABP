# Importo formularios
from django import forms

# Importo modelo User
from django.contrib.auth.models import User

# Importo formularios base de Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Importo modelo Proyecto
from .models import Proyecto


# FORM LOGIN (ARREGLA LOGIN)
class CustomAuthenticationForm(AuthenticationForm):

    # Aquí aplico clases a los campos
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


# FORM REGISTRO (YA ARREGLADO + COMPLETO)
class RegistroUsuarioForm(UserCreationForm):

    TIPO_USUARIO = (
        ('normal', 'Usuario normal'),
        ('admin', 'Administrador'),
    )

    tipo_usuario = forms.ChoiceField(
        choices=TIPO_USUARIO,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    proyecto = forms.ModelChoiceField(
        queryset=Proyecto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Aquí arreglo password fields
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
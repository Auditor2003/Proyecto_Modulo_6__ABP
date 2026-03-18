# Importo la función que me permite mostrar plantillas HTML
from django.shortcuts import render


# Aquí creo una vista llamada "home"
# Esta función será la encargada de mostrar la página principal del sistema
def home(request):

    # Aquí le digo a Django que muestre el archivo HTML que creé
    # Este archivo está dentro de: tareas/templates/tareas/home.html
    return render(request, 'tareas/home.html')

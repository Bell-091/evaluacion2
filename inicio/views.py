from django.shortcuts import render

def index(request):
    """
    Vista principal de la aplicación 'inicio'.
    Renderiza la página de bienvenida y presentación del proyecto.
    """
    contexto = {
        'titulo': 'Inicio - Sistema Django',
        'mensaje': 'Bienvenido a la plataforma de práctica de Django Templates.',
    }
    return render(request, 'inicio/index.html', contexto)

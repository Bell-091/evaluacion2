from django.shortcuts import render

def index(request):
    """
    Vista principal de la aplicación 'app1'.
    Instancia una lista de diccionarios que representan objetos de datos
    y los envía como contexto hacia el template.
    """
    lista_elementos = [
        {
            'id': 1,
            'nombre': 'Laptop Lenovo ThinkPad T14',
            'categoria': 'Computación',
            'precio': '$850.000',
            'stock': 8,
            'estado': 'Disponible'
        },
        {
            'id': 2,
            'nombre': 'Monitor Dell UltraSharp 27" 4K',
            'categoria': 'Monitores',
            'precio': '$380.000',
            'stock': 15,
            'estado': 'Disponible'
        },
        {
            'id': 3,
            'nombre': 'Teclado Mecánico Keychron K2 Wireless',
            'categoria': 'Periféricos',
            'precio': '$95.000',
            'stock': 22,
            'estado': 'Disponible'
        },
        {
            'id': 4,
            'nombre': 'Mouse Logitech MX Master 3S',
            'categoria': 'Periféricos',
            'precio': '$89.990',
            'stock': 4,
            'estado': 'Por encargo'
        },
        {
            'id': 5,
            'nombre': 'Audífonos Sony WH-1000XM5 Noise Cancelling',
            'categoria': 'Audio',
            'precio': '$299.990',
            'stock': 10,
            'estado': 'Disponible'
        },
        {
            'id': 6,
            'nombre': 'Servidor Rack Dell PowerEdge R650',
            'categoria': 'Infraestructura',
            'precio': '$3.450.000',
            'stock': 2,
            'estado': 'Por encargo'
        },
    ]

    contexto = {
        'titulo': 'Módulo 1: Catálogo de Elementos',
        'lista_elementos': lista_elementos,
    }
    return render(request, 'app1/index.html', contexto)

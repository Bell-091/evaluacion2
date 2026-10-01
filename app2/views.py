from django.shortcuts import render

def index(request):
    """
    Vista principal de la aplicación 'app2'.
    Renderiza la lista de servicios profesionales del sistema.
    """
    lista_servicios = [
        {
            'id': 101,
            'icono': '🚀',
            'nombre': 'Despliegue y Configuración Cloud',
            'descripcion': 'Automatización CI/CD, configuración de entornos productivos y servidores Linux.',
            'tarifa': '$250.000 / proyecto',
            'tiempo': '3 a 5 días hábiles',
            'estado': 'Activo'
        },
        {
            'id': 102,
            'icono': '🛡️',
            'nombre': 'Auditoría de Seguridad y Backend',
            'descripcion': 'Revisión exhaustiva de vulnerabilidades, inyecciones SQL, CSRF y middleware.',
            'tarifa': '$180.000 / informe',
            'tiempo': '2 días hábiles',
            'estado': 'Activo'
        },
        {
            'id': 103,
            'icono': '📊',
            'nombre': 'Optimización de Base de Datos y Queries',
            'descripcion': 'Indexación, refactorización de ORM Django y análisis de rendimiento.',
            'tarifa': '$150.000 / base de datos',
            'tiempo': '1 a 2 días',
            'estado': 'Activo'
        },
        {
            'id': 104,
            'icono': '📱',
            'nombre': 'Desarrollo de API RESTful con DRF',
            'descripcion': 'Endpoints autenticados con JWT, documentación Swagger/OpenAPI y pruebas unitarias.',
            'tarifa': '$320.000 / módulo',
            'tiempo': '1 semana',
            'estado': 'Activo'
        }
    ]

    contexto = {
        'titulo': 'Módulo 2: Catálogo de Servicios',
        'lista_servicios': lista_servicios,
    }
    return render(request, 'app2/index.html', contexto)

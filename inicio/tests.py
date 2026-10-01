from django.test import TestCase, Client
from django.urls import reverse

class InicioViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_inicio_view_status_code(self):
        response = self.client.get(reverse('inicio'))
        self.assertEqual(response.status_code, 200)

    def test_inicio_view_template_used(self):
        response = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(response, 'inicio/index.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Bienvenido a Mi Proyecto Django')

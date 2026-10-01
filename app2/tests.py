from django.test import TestCase, Client
from django.urls import reverse

class App2ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_app2_view_status_code(self):
        response = self.client.get(reverse('app2'))
        self.assertEqual(response.status_code, 200)

    def test_app2_view_templates_used(self):
        response = self.client.get(reverse('app2'))
        self.assertTemplateUsed(response, 'app2/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_app2_dynamic_services_context(self):
        response = self.client.get(reverse('app2'))
        self.assertIn('lista_servicios', response.context)
        servicios = response.context['lista_servicios']
        self.assertTrue(len(servicios) > 0)
        self.assertIsInstance(servicios[0], dict)
        self.assertIn('nombre', servicios[0])
        self.assertContains(response, servicios[0]['nombre'])

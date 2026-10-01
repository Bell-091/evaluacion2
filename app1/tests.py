from django.test import TestCase, Client
from django.urls import reverse

class App1ViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_app1_view_status_code(self):
        response = self.client.get(reverse('app1'))
        self.assertEqual(response.status_code, 200)

    def test_app1_view_templates_used(self):
        response = self.client.get(reverse('app1'))
        self.assertTemplateUsed(response, 'app1/index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_app1_dynamic_list_context_and_render(self):
        response = self.client.get(reverse('app1'))
        self.assertIn('lista_elementos', response.context)
        lista = response.context['lista_elementos']
        self.assertTrue(len(lista) > 0)
        self.assertIsInstance(lista[0], dict)
        self.assertIn('id', lista[0])
        self.assertIn('nombre', lista[0])
        # Verificar iteración e impresión del tag <li>ID: {{ item.id }} - {{ item.nombre }}</li>
        self.assertContains(response, f"ID: {lista[0]['id']} - {lista[0]['nombre']}")

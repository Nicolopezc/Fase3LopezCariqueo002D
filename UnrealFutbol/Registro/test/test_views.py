from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from Registro.models import Usuario

class UsuarioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_usuarios = 13 

        for Usuario_id in range(number_of_usuarios):
            Usuario.objects.create(
                nombre=f'alex{Usuario_id}',
                apellido=f'prueba {Usuario_id}',
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code,200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)             

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)

        self.assertTemplateUsed(response,'index.html')

      



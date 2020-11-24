from django.test import TestCase
from Registro.models import Usuario

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Usuario.objects.create(nombre='Pepito', apellido='Lopez')
    
    def test_name_label(self):
        unUsuario=Usuario.objects.get(id=1)
        field_label = unUsuario._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_apellido_label(self):
        unUsuario=Usuario.objects.get(id=1)
        field_label = unUsuario._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label,'apellido')

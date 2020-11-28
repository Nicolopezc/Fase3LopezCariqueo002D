from django.test import TestCase
from Registro.models import Usuario, Partido

class GenreModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        Usuario.objects.create(nombre='Pepito', apellido='Lopez')
    
    def test_name_label(self):
        unUsuario=Usuario.objects.get(id=1)
        field_label = unUsuario._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')

    def test_summary_label(self):
        unUsuario=Usuario.objects.get(id=1)
        field_label = unUsuario._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label,'apellido')

    def test_name_max_length(self):
        unUsuario=Usuario.objects.get(id=1)
        max_length = unUsuario._meta.get_field('nombre').max_length
        self.assertEquals(max_length,50)
    
    def test_summary_max_length(self):
        unUsuario=Usuario.objects.get(id=1)
        max_length = unUsuario._meta.get_field('apellido').max_length
        self.assertEquals(max_length,50)
        
    def test_get_absolute_url(self):
        unUsuario=Usuario.objects.get(id=1)
        self.assertEquals(unUsuario.get_absolute_url(), '/Registro/usuario/1')    

class PartidoModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        U = Usuario.objects.create(nombre='pepito', apellido='lopez')
        partidos=Partido.objects.create(local='everton', visita='malaya',estadio='en la esquina de mi casa',fecha_partido='2020-11-30',competicion='copa del mundo mundial')        

    def test_title_label(self):
        Partidos=Partido.objects.get(local= 'everton')
        field_label = Partido._meta.get_field('local').verbose_name
        self.assertEquals(field_label,'local')
    
    def test_title_max_length(self):
        Partidos=Partido.objects.get(local='everton')
        max_length = Partido._meta.get_field('local').max_length
        self.assertEquals(max_length,50)



    
    
    def test_title_label(self):
        Partidos=Partido.objects.get(visita= 'malaya')
        field_label = Partido._meta.get_field('visita').verbose_name
        self.assertEquals(field_label,'visita')
    
    def test_title_max_length(self):
        Partidos=Partido.objects.get(visita='malaya')
        max_length = Partido._meta.get_field('visita').max_length
        self.assertEquals(max_length,50)    



    def test_title_label(self):
        Partidos=Partido.objects.get(estadio= 'en la esquina de mi casa')
        field_label = Partido._meta.get_field('estadio').verbose_name
        self.assertEquals(field_label,'estadio')
    
    def test_title_max_length(self):
        Partidos=Partido.objects.get(estadio='en la esquina de mi casa')
        max_length = Partido._meta.get_field('estadio').max_length
        self.assertEquals(max_length,100) 



    
    def test_title_label(self):
        Partidos=Partido.objects.get(fecha_partido= '2020-11-30')
        field_label = Partido._meta.get_field('fecha_partido').verbose_name
        self.assertEquals(field_label,'fecha partido')


    def test_title_label(self):
        Partidos=Partido.objects.get(competicion= 'copa del mundo mundial')
        field_label = Partido._meta.get_field('competicion').verbose_name
        self.assertEquals(field_label,'competicion')
    
    def test_title_max_length(self):
        Partidos=Partido.objects.get(competicion='copa del mundo mundial')
        max_length = Partido._meta.get_field('competicion').max_length
        self.assertEquals(max_length,100)     
    
    
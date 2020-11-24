from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registro/',views.registro, name='registro'),
    path('terminos/',views.terminos,name='terminos'),
    path('galeria/', views.galeria, name='galeria'),
    path('apuesta/', views.apuesta, name='apuesta'),
    path('usuario/<int:pk>', views.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('partidos/',views.PartidoListView.as_view(), name='partidos'),
    path('partidos/<int:pk>', views.PartidoDetailView.as_view(), name='partido-detail'),
]

urlpatterns+=[
    path('usuario/create/', views.UsuarioCreate.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/update/', views.UsuarioUpdate.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/delete/', views.UsuarioDelete.as_view(), name='usuario_delete'),
    path('partido/create/', views.PartidoCreate.as_view(), name='partido_create'),
    path('partido/<int:pk>/update/', views.PartidoUpdate.as_view(), name='partido_update'),
    path('partido/<int:pk>/delete/', views.PartidoDelete.as_view(), name='partido_delete'),

]

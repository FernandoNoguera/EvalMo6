from django.urls import path
from . import views

app_name = "clinica_fenix_01"

urlpatterns = [
    path("", views.inicio, name= "index"),
    path("pagina_privada/", views.private_page, name ="portal_privado" ),
    path("usuario_nuevo/", views.CrearUsuario.as_view(), name="nuevo_usuario"),
    path("lista_usuarios/", views.ListaPacientes.as_view(), name="lista_usuario"),
    path("<int:pk>/borrar/",views.EliminarPaciente.as_view(), name="eliminar_cliente"),
    path("<int:pk>/editar/",views.EditarPaciente.as_view(), name="editar_cliente"),
    path("examen_nuevo/", views.CrearExamen.as_view(), name="nuevo_examen"),
    path("examen_usuarios/", views.ListaExamenes.as_view(), name="lista_examen"),
    path("<int:pk>/borrar_examen/",views.EliminarExamen.as_view(), name="eliminar_examen"),
    path("<int:pk>/editar_examen/",views.EditarExamen.as_view(), name="editar_examen"),
    path("<int:pk>/examen_cliente/", views.examen_cliente, name="examen_cliente"),
    path("registro", views.Registro.as_view(), name="registro"),
]

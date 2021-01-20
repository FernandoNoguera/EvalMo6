from django.urls import path
from . import views

app_name = "clinica_fenix_01"

urlpatterns = [
    path("", views.inicio, name= "index"),
    path("login/", views.login, name = "login" ),
    path("pagina_privada/", views.private_page, name ="portal_privado" ),
    path("usuario_nuevo/", views.CrearUsuario.as_view(), name="nuevo_usuario" ),
    path("lista_usuarios/", views.ListaPacientes.as_view(), name="lista_usuario"),
    path("<int:pk>/borrar/",views.EliminarPaciente.as_view(), name="eliminar_cliente"),
    path("<int:pk>/editar/",views.EditarPaciente.as_view(), name="eliminar_cliente"),
    path("<id>/render/", views.render_cliente, name="render_cliente"),
]

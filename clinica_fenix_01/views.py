from django.shortcuts import render, redirect 
from django.conf import settings
#from .forms import ContactForm
import json
from .models import Usuario, Examen
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
#import requests
from django.core.mail import EmailMessage
#from django.shortcuts import render, redirect
#import random
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


def inicio(request):
    return render(request, 'clinica_fenix_01/index.html')

@login_required(login_url='/accounts/login/')
def private_page(request):
    dic1 = {}
    edad = []
    apellidos = []
    usuarios = Usuario.objects.all().values()
    for i in usuarios:
        for key,value in i.items():
            dic1 = key,value
            if key == 'edad':
                edad.append(value)
            elif key == 'apellido_paterno':
                apellidos.append(value)
            else:
                continue

    try:
        usuario_id = request.user.id #OBTENER ID DEL USUARIO QUE ESTA VISITANDO LA VISTA
        perfil = Usuario.objects.filter(usuario_id=usuario_id).values()[0]
    except:
        perfil= 0

    context = {'edad': edad, 'nombre':apellidos , 'usuarios': usuarios,'my_id':usuario_id, 'perfil':perfil }
    return render(request, 'clinica_fenix_01/PagePrivate.html', context)


class ListaPacientes(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model= Usuario
    template_name= "clinica_fenix_01/lista_usuario.html"
    context_object_name = "Usuario"
    #extra_context = {'usuario': usuarios }


class CrearUsuario(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model = Usuario
    template_name= "clinica_fenix_01/new_user.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EliminarPaciente(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model = Usuario
    template_name= "clinica_fenix_01/eliminar_cliente.html"
    context_object_name = "Usuario"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')


class EditarPaciente(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model = Usuario
    template_name= "clinica_fenix_01/editar_cliente.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_usuario')

    
class ListaExamenes(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model= Examen
    template_name= "clinica_fenix_01/lista_examen.html"
    context_object_name = "Examenes"
    #extra_context = {''}


class CrearExamen(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model = Examen
    template_name= "clinica_fenix_01/new_examen.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')


class EliminarExamen(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    login_url= 'clinica_fenix_01:index'
    model = Examen
    template_name= "clinica_fenix_01/eliminar_examen.html"
    context_object_name = "Examenes"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')


class EditarExamen(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'user.Usuario.rol=ADMINISTRADOR'
    model = Examen
    template_name= "clinica_fenix_01/editar_examen.html"
    fields = '__all__'
    success_url = reverse_lazy('clinica_fenix_01:lista_examen')

@login_required(login_url='/accounts/login/')
def examen_cliente(request, pk):
    dic1 = {}
    data_num = []
    usuarios = Usuario.objects.all().values()
    examen = Examen.objects.all().values()
    for cliente in usuarios:
        if int(cliente['id']) == int(pk):
            cliente_datos = cliente
    #### dato 1 Plaquetas
    for cliente in examen:
        if int(cliente['usuario_id_id']) == int(pk):
            for key,value in cliente.items():
                dic1 = key,value
                if key == 'plaquetas':
                    data_num.append(value)
                elif key == 'globulos_blancos':#### dato 2 G blancos
                    data_num.append(value)
                elif key == 'globulos_rojos':##### dato 3 G rojos
                    data_num.append(value)
                elif key == 'hematocritos': ##### dato 4 Hematocrito
                    data_num.append(value)
                else:
                    continue
        else:
            pass

    context = {'id':id, 'cliente': cliente_datos, 'data_num': data_num , 'examen': examen }
    return render(request, 'clinica_fenix_01/render_cliente.html', context)


class Registro(generic.CreateView):

    form_class = UserCreationForm
    template_name= "clinica_fenix_01/registro.html"
    success_url = reverse_lazy('clinica_fenix_01:index')

